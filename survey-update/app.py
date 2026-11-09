import os
import secrets
from contextlib import contextmanager

import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
# Additional environment variables are not needed. Restarting invalidates sessions.
app.secret_key = secrets.token_bytes(32)
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax", MAX_CONTENT_LENGTH=64 * 1024)

# Counts read from the supplied survey chart: uncomfortable + very uncomfortable.
SURVEY_COUNTS = {'metallic': 13, 'chewing': 12, 'snoring': 12, 'sneezing': 9, 'insects': 9}

SOUNDS = {
    'metallic': ('金属音', '金属がぶつかる・こすれる音'),
    'chewing': ('咀嚼音', '食べ物をかむ音'),
    'snoring': ('いびき', '睡眠中のいびきの音'),
    'sneezing': ('大きいくしゃみ', '突然の大きなくしゃみの音'),
    'insects': ('虫の音', '虫の鳴き声や羽音'),
    'conversation': ('会話', '人の声・隣の席の話し声'),
    'announcement': ('アナウンス', '駅や店内の案内'),
    'alarm': ('警報・サイレン', '大切な安全の音'),
    'traffic': ('交通音', '車・電車の走行音'),
    'dishes': ('食器の音', 'カップや皿が触れる音'),
    'keyboard': ('キーボード', 'タイピング・クリック音'),
    'music': ('音楽', '店内BGMなど'),
    'nature': ('自然の音', '鳥・雨・風の音'),
}


@contextmanager
def database():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute('SELECT current_schema() AS schema_name')
                schema = cur.fetchone()['schema_name']
                if not schema:
                    raise RuntimeError('current_schema() が取得できません。接続先の search_path を確認してください。')
                # Identifier quoting confines unqualified table names to current_schema().
                cur.execute(sql.SQL('SET LOCAL search_path TO {}').format(sql.Identifier(schema)))
                yield cur
    finally:
        conn.close()


@app.before_request
def csrf_check():
    session.setdefault('csrf', secrets.token_urlsafe(32))
    if request.method == 'POST':
        token = request.form.get('csrf', '')
        if not secrets.compare_digest(token.encode('utf-8'), session['csrf'].encode('utf-8')):
            abort(400, 'ページを更新してから再度操作してください。')


@app.context_processor
def shared():
    return {'sounds': SOUNDS, 'survey_counts': SURVEY_COUNTS, 'csrf': session.get('csrf', '')}


@app.errorhandler(psycopg2.Error)
@app.errorhandler(KeyError)
@app.errorhandler(RuntimeError)
def database_error(error):
    app.logger.error('Database unavailable: %s', type(error).__name__)
    return render_template('settings.html', rules={}, error='設定を読み込めませんでした。DATABASE_URL・接続先・テーブル作成状況を確認してください。', unavailable=True), 503


def parse_rules(form):
    values = []
    for key in SOUNDS:
        action = form.get('action_' + key, '')
        if action not in ('reduce', 'keep', 'protect'):
            raise ValueError('すべての音の扱い方を選択してください。')
        if key == 'alarm' and action != 'protect':
            raise ValueError('警報・サイレンは「必ず残す」に設定してください。')
        raw = form.get('strength_' + key, '')
        try:
            strength = int(raw)
        except ValueError:
            raise ValueError('低減の強さは0〜100の整数で指定してください。') from None
        if not 0 <= strength <= 100:
            raise ValueError('低減の強さは0〜100で指定してください。')
        values.append((key, action, strength if action == 'reduce' else 0))
    return values


@app.route('/', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        try:
            values = parse_rules(request.form)
        except ValueError as error:
            draft = {}
            for key in SOUNDS:
                action = request.form.get('action_' + key, 'keep')
                if action not in ('reduce', 'keep', 'protect'):
                    action = 'keep'
                if key == 'alarm':
                    action = 'protect'
                try:
                    strength = max(0, min(100, int(request.form.get('strength_' + key, '50'))))
                except ValueError:
                    strength = 50
                draft[key] = {'action': action, 'strength': strength}
            return render_template('settings.html', rules=draft, error=str(error)), 400
        with database() as cur:
            # All sound settings are saved in one transaction.
            for key, action, strength in values:
                cur.execute(
                    'INSERT INTO sound_settings (sound_key, action, strength) VALUES (%s, %s, %s) '
                    'ON CONFLICT (sound_key) DO UPDATE SET action = EXCLUDED.action, '
                    'strength = EXCLUDED.strength, updated_at = now(), deleted_at = NULL',
                    (key, action, strength),
                )
        flash('音の設定を保存しました。')
        return redirect(url_for('settings'))
    with database() as cur:
        cur.execute('SELECT sound_key, action, strength FROM sound_settings WHERE deleted_at IS NULL')
        rules = {row['sound_key']: row for row in cur.fetchall()}
    return render_template('settings.html', rules=rules, error=None)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)

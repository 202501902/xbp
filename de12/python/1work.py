#ーーーーーGAMESTARTーーーーー
print("===============🌺うちなんちゅレベルクイズ🌺===============")
name=input("あなたの名前を入力してください： ")
print()
print(name,"さん！これから方言やうちなんちゅの日常に関する問題を出すよ！")
print("あなたのうちなんちゅレベルはどれくらいかな？？")
print("正解だと思う選択肢の番号を全角で入力してね！")
print()
score=0

#Q1
print()
print("Q1.「ちーち－かーかーする」とはどういう状態？")
print("１. 視界が悪くなってちかちかする状態")
print("２. ぱさぱさして喉が渇いた状態")
print("３. 全力で走って息が切れた状態")
ans=input("➔ あなたの答え： ")
if ans=="２":
    print()
    print("正解！サーターアンダギーを食べたあとはちーちーかーかーするよ😿")
    score+=1
else:
    print()
    print("おしい！正解は「２. ぱさぱさして喉が渇いた状態」でした！")

#Q2
print()
print("Q2. 結婚式でみんなで踊るのは何？")
print("１. 盆踊り")
print("２. カチャーシー")
print("３. フラダンス")
ans=input("➔ あなたの答え： ")
if ans=="２":
    print()
    print("正解！あなたも一緒に踊ろう🎶🎶")
    score+=1
else:
    print()
    print("残念！正解は「２. カチャーシー」でした！")

#Q3
print()
print("Q3. 「ハーリー」は何の行事？")
print("１. 綱引き")
print("２. 獅子舞見物")
print("３. 船漕ぎのレース")
ans=input("➔ あなたの答え： ")
if ans=="３":
    print()
    print("正解！毎年沖縄各地で開催されるよ⭐")
    score+=1
else:
    print()
    print("間違い！正解は「３. 船漕ぎのレース」でした！")

#Q4
print()
print("Q4.「うりひゃーさーさー」とはどういうときに使う言葉？")
print("１. 驚いたとき")
print("２. 面白かったとき")
print("３. 怒ったとき")
ans=input("➔ あなたの答え： ")
if ans=="１":
    print()
    print("正解！私の祖父母がよく驚いたときに使ってるよ👍")
    score+=1
else:
    print()
    print("もうちょい！正解は「１. 驚いたとき」でした！")

#Q5
print()
print("Q5.「ヒラヤーチー」はどんな食べ物？")
print("１. 沖縄風たこ焼き")
print("２. 沖縄風お好み焼き")
print("３. 沖縄風ピザ")
ans=input("➔ あなたの答え： ")
if ans=="２":
    print()
    print("正解！オイスターソースをかけたらとても美味しいよ😋")
    score+=1
else:
    print()
    print("ハズレ～！正解は「２. 沖縄風お好み焼き」でした！")

#ー結果ー
print()
print("===============✨結果発表✨===============")
print(name, "さんの正解数は" ,score, "問でした！")
if score==5:
    print("うちなんちゅレベルMAX！まぎーうちなんちゅだね🌺")
elif score>=4:
    print("いい感じ！うちなんちゅ予備軍だね🌺")
elif score>=2:
    print("うちなんちゅ見習いだね！まだまだこれからさ～🌺")
else:
    print("まだまだ本土んちゅだね！")
print()
print("🌺お付き合いいただきありがとう！にふぇ～で～びたん🌺")
#ーーーーーFINISHーーーーー
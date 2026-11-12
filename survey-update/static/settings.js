document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#settings-form');
  const state = document.querySelector('#save-state');
  document.querySelectorAll('.sound-card').forEach(card => {
    const range = card.querySelector('input[type="range"]');
    if (!range) return;
    const output = card.querySelector('output');
    const sync = () => {
      const reduce = card.querySelector('input[type="radio"]:checked').value === 'reduce';
      card.classList.toggle('is-reducing', reduce);
      // Keep the slider submitted even when its value does not apply.
      range.setAttribute('aria-disabled', String(!reduce));
      range.tabIndex = reduce ? 0 : -1;
      output.textContent = range.value + '%';
      range.setAttribute('aria-valuetext', range.value + 'パーセント');
    };
    card.querySelectorAll('input').forEach(input => input.addEventListener('input', sync));
    sync();
  });
  form.addEventListener('input', () => { state.textContent = '変更はまだ保存されていません'; });
  form.addEventListener('submit', () => { state.textContent = '保存しています…'; });
});

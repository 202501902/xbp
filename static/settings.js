document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#settings-form');
  if (!form) return;
  const boxes = [...form.querySelectorAll('input[name="reduce_sounds"]')];
  const counter = document.querySelector('#selected-count');
  const state = document.querySelector('#save-state');
  const sync = () => { counter.textContent = boxes.filter(box => box.checked).length; };
  boxes.forEach(box => box.addEventListener('change', () => {
    sync();
    state.textContent = '変更はまだ保存されていません。';
  }));
  form.addEventListener('submit', () => { state.textContent = '音環境を保存しています…'; });
  sync();
});

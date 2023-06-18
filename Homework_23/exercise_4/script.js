const Input = document.getElementById('input');
const PlusBtn = document.getElementById('plus');

PlusBtn.addEventListener('click', function() {
  const PlusInput = document.createElement('input');
  PlusInput.type='text';
  Input.parentNode.appendChild(PlusInput);
});
const Input = document.getElementById('input');
const CloneBtn = document.getElementById('clone-btn');

CloneBtn.addEventListener('click', function() {
  const ClonedInput = Input.cloneNode(true);
  Input.parentNode.appendChild(ClonedInput);
});
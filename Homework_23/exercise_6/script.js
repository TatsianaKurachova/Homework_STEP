let Input = document.getElementById('input');
const CheckBtn = document.getElementById('check-btn');

CheckBtn.addEventListener('click', function() {
  let Arr = Input.value.split(',').map(Number);
  let FiveInArray = false;

  for (let i = 0; i < Arr.length; i++) {
    if (Arr[i] === 5) {
      FiveInArray = true;
      break;
    }
  }

  if (FiveInArray) {
    console.log('Да');
  } else {
    console.log('Нет');
  }
});
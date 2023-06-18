let Input = document.getElementById('input');
const CheckBtn = document.getElementById('check-btn');

CheckBtn.addEventListener('click', function() {
  let Arr = Input.value.split(',').map(Number);
  let isThereSameNumbers = false;

  for (let i = 0; i < Arr.length - 1; i++) {
    if (Arr[i] === Arr[i+1]) {
      isThereSameNumbers = true;
      break;
    }
  }

  if (isThereSameNumbers) {
    console.log('Да');
  } else {
    console.log('Нет');
  }
});




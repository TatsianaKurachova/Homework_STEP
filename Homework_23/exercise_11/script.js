let Arr = [1, -2, 3, -4, 5, -6, -100, 200];
let Sum = 0;
for(let i = 0; i < Arr.length; i++) {
    if(Arr[i] > 0) {
        Sum += Arr[i];
    }
}
let ResultElement = document.getElementById("result");
ResultElement.innerText = "Сумма положительных чисел: " + Sum;
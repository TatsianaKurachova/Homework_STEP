const Arr = [2, 3, 4, 5];
let product = 1;

for (let i = 0; i < Arr.length; i++) {
  product*=Arr[i];
}
console.log(product);

const result = document.getElementById("result").innerHTML =
    "Произведение элементов массива: " + product;
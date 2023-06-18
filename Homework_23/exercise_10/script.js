let Numbers= [];
for (let i = 1; i <= 100; i++) {
    Numbers.push(i);
}

let List = document.getElementById("myList");

for (let i = 0; i < Numbers.length; i++) {
    let New = document.createElement("li");
        New.innerText = Numbers[i];
        List.appendChild(New);
}

let ListTwo = document.getElementById("myListtwo");

for (let i = 10; i <= 32; i++) {
    let NewTwo = document.createElement("li");
    NewTwo.innerText = Numbers[i];
    ListTwo.appendChild(NewTwo);
}


let NumbersThree= [];

for (let i = 0; i <= 100; i++) {
    if (i % 2 === 0) {
    NumbersThree.push(i);
    }
}

let ListThree = document.getElementById("myListthree");

for (let i = 0; i < NumbersThree.length; i++) {
    let NewThree = document.createElement("li");
    NewThree.innerText = NumbersThree[i];
    ListThree.appendChild(NewThree);
}

let sum = 0;
for (let i = 0; i <= 100; i++) {
    sum += i;
}
let resultElement = document.getElementById("result");
resultElement.innerText = "Сумма чисел от 0 до 100: " + sum;
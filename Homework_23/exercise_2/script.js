const elem = document.querySelector("#elem")
const parent = elem.parentNode;
console.log(elem.classList);

// elem.classList.add("www");
// console.log(elem.classList); 

// elem.classList.remove("www");
// console.log(elem.classList);

// if(elem.classList.contains("www")){
//   console.log('Класс есть');
// }
// else {
//   console.log('Класса нет');
// }

if(elem.classList.contains('www')){
  elem.classList.remove('www');
}
else {
  elem.classList.add('www');
}

console.log(elem.classList.length);

elem.classList.forEach(function(className) {
  alert(className);
});


parent.style.backgroundColor = 'red';
const search = document.getElementById('text')
console.log(search.value)
const BTN1 = document.getElementById('btn1')
const output = document.getElementById('output')
const BTN2 = document.getElementById('btn2')
const BTN3 = document.getElementById('btn3')

BTN1.addEventListener("click", myFunction)

function myFunction() {
  console.log(search.value)
  if (search.value===""){
    output.innerHTML="Вы ничего не ввели"
  } else {
    output.innerHTML=search.value
  }
}

BTN2.addEventListener("click", register)

function register() {
  var name = document.getElementById('login').value
  var phone = document.getElementById('phone').value
  alert(name + ', вы успешно зарегистрированы')
}

BTN3.addEventListener("click", checkFields)

function checkFields() {
  var year = document.getElementById('year').value
  var vol = document.getElementById('vol').value
  var message = ''
  if (year === '') {
    message += 'Не заполнено поле "Год выпуска"\n'
  }
  if (vol === '') {
    message += 'Не заполнено поле "Объем двигателя"\n'
  }
  if (message === '') {
    message = 'Все поля заполнены'
  }
  document.getElementById('message').innerText = message
}
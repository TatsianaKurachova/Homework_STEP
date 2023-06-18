const div1=document.getElementById('div1')
const div2=document.getElementById('div2')

function red() {
  this.style.backgroundColor = 'red';
  this.removeEventListener('click', red);
  this.addEventListener('click', green);
}

function green() {
  this.style.backgroundColor = 'green';
  this.removeEventListener('click', green);
  this.addEventListener('click', red);
}

div1.addEventListener('click', red);
div2.addEventListener('click', red);
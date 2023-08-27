let counter = document.querySelector(".counter")
let count = 0

function add_1(){
    alert("Вы нажали на кнопку")
    count += 1
    counter.textContent = count
}
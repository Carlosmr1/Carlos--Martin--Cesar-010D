const count = document.getElementById("contador-productos");
const agregar = document.getElementById("agregar");
let number = 0;

agregar.addEventListener("click", ()=>{
    number++;
    count.innerHTML = number;
})
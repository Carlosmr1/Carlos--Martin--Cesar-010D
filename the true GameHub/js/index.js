

$('#submit').click(function() {

    var regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;

    if (regex.test($('#correo').val().trim())) {
        
    } else {
        alert('La direccón de correo no es válida');
    }
    //validar usuario
    if($('#user').val() === "" || $('#user').val()=== null){
        alert("Debe ingresar un Nombre de usuario");
        
        return false;
        }

    // validar contraseña
if ($('#psw').val() === "" || $('#psw').val() === null) {
    alert("Debe ingresar una contraseña");
    return false;
}
// validar confirmación de contraseña
if ($('#confPsw').val() === "" || $('#confPsw').val() === null) {
    alert("Debe confirmar la contraseña");
    return false;
    }
    
if ($('#psw').val() !== $('#confPsw').val() ) {
alert("Las contraseñas no coinciden");
return false;
}

});
// function enviarFormulario()
// {
// var correo = document.getElementById("correo");
// var usuario = document.getElementById("user");
// var contrasena = document.getElementById("psw");
// var confirmarContrasena = document.getElementById("confPsw");
// var correoform = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
// //validar usuario
// if(usuario.value === "" || usuario.value === null){
//     alert("Debe ingresar un Nombre de usuario");
    
//     return false;
//     }

// // validar contraseña
// if (contrasena.value === "" || contrasena.value === null) {
//     alert("Debe ingresar una contraseña");
//     return false;
// }
// // validar confirmación de contraseña
// if (confirmarContrasena.value === "" || confirmarContrasena.value === null) {
//     alert("Debe confirmar la contraseña");
//     return false;
//     }
    
// if (confirmarContrasena.value !== contrasena.value ) {
// alert("Las contraseñas no coinciden");
// return false;
// }
// // validar correo
// if(correo.value.match(correoform))
// {

// return true;
// }
// else
// {
// alert("Debe ingresar un correo electronico valido");

// return false;
// }


// } 

const count = document.getElementById("contador-productos");
const agregar = document.getElementById("agregar");
let number = 0;



const listaProductos = [
    {
        id:1,
        nombre: "Escape from Tarkov",
        precio: 27000
    },
    {
        id:2,
        nombre:"Minecraft",
        precio:20000
    },
    {
        id: 3,
        nombre:"The Last of Us",
        precio:30900
    },
    {
        id: 4,
        nombre:"Project Zomboid",
        precio:17000
    },
    {
        id: 5,
        nombre:"Cult of The Lamb",
        precio: 14909
    }
];

listaProductos.forEach((producto)=>{
    const {id, nombre,precio} = producto
});


function agregarC(id){
    const item = listaProductos.find((producto) => producto.id === id);
    carrito.push(item);
    mostrarCarrito();
    console.log(carrito);
}
const contenedor = document.querySelector('.modal-content');
const mostrarCarrito= ()=>{
    
    carrito.forEach((producto) => {
        const {id, nombre, precio} = producto;

        contenedor.innerHTML += '<p id="carro">'+nombre + " " + "$" + precio +"</p> <br>";
    })
    number= number+1;
    count.innerHTML = number;
    guardarCarrito();
}

function eliminarProducto(id){
    const juegoId = id
    carrito = carrito.filter((juego) => juego.id !== juegoId)
    mostrarCarrito()
}

function guardarCarrito(){
    localStorage.setItem("carrito", JSON.stringify(carrito));
}
const carrito = []




var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function close() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

const finCompra = document.getElementById("comprarbtn");
function finalizarCompra(){
    modal.style.display = "none";
    alert("GRACIAS POR SU COMPRA :D")
    contenedor.innerHTML = '<button onclick="finalizarCompra()" id="comprarbtn"> COMPRAR</button>';
    count.innerHTML = "0";
    carrito.length = 0;
    number = 0;
    console.log(carrito);
}

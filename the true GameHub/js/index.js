
function enviarFormulario()
{
var correo = document.getElementById("correo");
var usuario = document.getElementById("user");
var contrasena = document.getElementById("psw");
var confirmarContrasena = document.getElementById("confPsw");
var correoform = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
//validar usuario
if(usuario.value === "" || usuario.value === null){
    alert("Debe ingresar un Nombre de usuario");
    
    return false;
    }

// validar contraseña
if (contrasena.value === "" || contrasena.value === null) {
    alert("Debe ingresar una contraseña");
    return false;
}
// validar confirmación de contraseña
if (confirmarContrasena.value === "" || confirmarContrasena.value === null) {
    alert("Debe confirmar la contraseña");
    return false;
    }
    
if (confirmarContrasena.value !== contrasena.value ) {
alert("Las contraseñas no coinciden");
return false;
}
// validar correo
if(correo.value.match(correoform))
{

return true;
}
else
{
alert("Debe ingresar un correo electronico valido");

return false;
}


} 

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
    }
];

listaProductos.forEach((producto)=>{
    const {id, nombre,precio} = producto
});


function agregarC(id){
    const item = listaProductos.find((producto) => producto.id === id);
    carrito.push(item);
    mostrarCarrito();
}
const mostrarCarrito= ()=>{
    const contenedor = document.getElementById("divi");
    carrito.forEach((prod) => {
        const {id, nombre, precio} = prod;
        contenedor.innerHTML = nombre;
    })
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


agregar.addEventListener("click", ()=>{
    number++;
    count.innerHTML = number;
});


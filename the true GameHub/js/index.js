
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
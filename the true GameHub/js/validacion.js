
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



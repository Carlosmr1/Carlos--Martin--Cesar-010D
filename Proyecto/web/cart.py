class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    

    def agregar(self, producto):
        nombre = str(producto.nombre)
        if nombre not in self.carrito.keys():
            self.carrito[nombre]={
                "producto_nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[nombre]["cantidad"]+= 1
            self.carrito[nombre]["acumulado"]+= producto.precio
        self.guardarCarrito()

    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        nombre = str(producto.nombre)
        if nombre in self.carrito:
            del self.carrito[nombre]
            self.guardarCarrito()
    
    def restar(self, producto):
        nombre = str(producto.nombre)
        if nombre in self.carrito.keys():
            self.carrito[nombre]["cantidad"]-= 1
            self.carrito[nombre]["acumulado"]-= producto.precio
            if self.carrito[nombre]["cantidad"]<= 0: self.eliminar(producto)
            self.guardarCarrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
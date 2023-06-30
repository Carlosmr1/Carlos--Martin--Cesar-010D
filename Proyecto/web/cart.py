class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    

    def agregarT(self, tablegames):
        nombre = str(tablegames.nombre)
        if nombre not in self.carrito.keys():
            self.carrito[nombre]={
                "tablegames_nombre": tablegames.nombre,
                "precio": tablegames.precio,
                "marca": tablegames.marca,
                "cantidad": 1,
            }
        else:
            self.carrito[nombre]["cantidad"]+= 1
            self.carrito[nombre]["precio"]+= tablegames.precio
        self.guardarCarrito()

    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, tablegames):
        nombre = str(tablegames.nombre)
        if nombre in self.carrito:
            del self.carrito[nombre]
            self.guardarCarrito()
    
    def restar(self, tablegames):
        nombre = str(tablegames.nombre)
        if nombre in self.carrito.keys():
            self.carrito[nombre]["cantidad"]-= 1
            self.carrito[nombre]["precio"]-= tablegames.precio
            if self.carrito[nombre]["cantidad"]<= 0: self.eliminar(tablegames)
            self.guardarCarrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
class cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session 
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    def add(self, product):
        if str(Tablegames.nombre) not in self.cart.keys():
            self.cart[Tablegames.nombre] = {
                "tablegames.nombre" = Tablegames.nombre,

            }
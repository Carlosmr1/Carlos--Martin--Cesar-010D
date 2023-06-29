from django.contrib import admin
from .models import Videogames, Marca, Tablegames


# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca"]

admin.site.register(Marca)
admin.site.register(Tablegames, ProductosAdmin )
admin.site.register(Videogames, ProductosAdmin)
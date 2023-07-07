from django.contrib import admin
from .models import Marca, Productos, User, Categoria


# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca","categoria"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca"]

admin.site.register(Marca)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Categoria)
admin.site.register(User)
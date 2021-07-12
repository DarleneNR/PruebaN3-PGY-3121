from django.contrib import admin
from .models import Categoria, Producto, Venta, Cliente, Usuario, Suscrito

# Register your models here.
# Permite manejar o manipular el modelo por completo.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Suscrito)
from django.db import models

# Create your models here.
# Modelo para la Categorias de los Productos
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name="Identificador del Producto")
    nombreCategoria = models.CharField(max_length=70, verbose_name="Nombre Categoría", help_text="Introduzca el tipo de Categoría")

    def __str__(self):
        return self.nombreCategoria

# Modelo para los Productos 
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Identificador del Producto")
    nombreProducto = models.CharField(max_length=70, verbose_name="Nombre Producto", help_text="Introduzca el nombre")
    precioUnidad = models.IntegerField(verbose_name="Precio Producto", help_text="Introduzca el precio por prodcuto")
    cantStock = models.IntegerField(verbose_name="Stock disponible", help_text="Introduzca cantidad de Stock disponible")
    idCategoria = models.ForeignKey(Categoria, on_delete=models.SET('CategoríaEliminada'), help_text="Selecciona la Categoría")

    def __str__(self):
        return self.nombreProducto

# Modelo para las Ventas
class Venta(models.Model):
    nroVenta = models.AutoField(primary_key=True, verbose_name="Identificador de la Venta")
    idProducto = models.ForeignKey(Producto, on_delete=models.SET('ProductoEliminado'), help_text="Selecciona Producto")
    cantidad = models.CharField(max_length=20, null=True, blank=True, verbose_name="Cantidad", help_text="Introduzca la cantidad de los productos a comprar")
    montoVenta = models.IntegerField(verbose_name="Monto Total a pagar")

    def __str__(self):
        return self.nroVenta

# Modelo para Clientes
class Cliente(models.Model):
    nroRutCli = models.IntegerField(primary_key=True, verbose_name="Número Rut del cliente")
    dvRun = models.CharField(max_length=1, verbose_name="Dígito Verificador", help_text="Introduzca el dígito verificador de su rut")
    nombreCli = models.CharField(max_length=70, verbose_name="Nombre Cliente", help_text="Introduzca su nombre completo")
    apellidocli = models.CharField(max_length=80, verbose_name="Apellido Cliente", help_text="Introduzca su(s) apellido(s)")

    def __str__(self):
        return self.nroRutCli

# Modelo para Usuarios (Clientes Registrados)
class Usuario(models.Model):
    idUser = models.AutoField(primary_key=True, verbose_name="Identificador del Usuario")
    nombreUser = models.CharField(unique=True, max_length=30, verbose_name="Nombre de usuario", help_text="Introduzca el nombre de usuario")
    passwordUser = models.CharField(max_length=10, verbose_name="Contraseña", help_text="Introduzca la contraseña")
    nroRutCli = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Número Rut sin dígito verificador")

    def __str__(self):
        return self.nombreUser

# Modelo para Usuarios Suscritos / Usuarios que hayan donado 
class Suscrito(models.Model):
    idSuscripcion = models.AutoField(primary_key=True, verbose_name="Identificador de la Suscripción")
    nombreUser = models.CharField(unique=True, max_length=30, verbose_name="Nombre de usuario", help_text="Introduzca el nombre de usuario")
    fechaSuscripcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha en la que el usuario se suscribió")

    def __str__(self):
        return self.idSuscripcion
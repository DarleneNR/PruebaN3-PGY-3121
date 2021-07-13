from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Venta, Cliente, Usuario, Suscrito

# Create your views here.
# Pagina Inicial
def index(request):
    # Mostrar los Productos a la Venta
    productos = Producto.objects.all()
    datosObtenidos = {
        'productos': productos
    }
    return render(request, 'core/index.html', datosObtenidos)

# Login de usuarios previamente registrados
def loginRegisterUser(request):
    return render(request,'core/loginRegisterUser.html')

# Validación: Existe el usuario en la BD
def verificacionUser (request):
    if request.method == 'POST':
        username = request.POST['usernmaneCli']
        password = request.POST['passwordUser']

        selUsuario = Usuario.objects.get(nombreUser=username, passwordUser=password)

        """ # Enviando el nombre de usuario para acciones ha realizar en la página principal
        datosObtenidos = {
            'selUsuario': selUsuario
        }

    return render(request, 'core/index.html', datosObtenidos) """
    return redirect('index.html')

# Registro de nuevos Usuarios
def registroUser (request):
    if request.method == 'POST':
        numRut = request.POST['nroRutCli']
        dvRut = request.POST['dvRun']
        nombres = request.POST['nombreCli']
        apellidos = request.POST['apellidocli']
        nombreUser = request.POST['nombreUser']
        passwordUser = request.POST['passwordUser']

        # 1. Agregando datos a la taba Cliente
        Cliente.objects.create(nroRutCli=numRut, dvRun=dvRut, nombreCli=nombres, apellidocli=apellidos)

        # 2.- Agregando datos a la tabla Usuario
        selCliente = Cliente.objects.get(nroRutCli=numRut)
        Usuario.objects.create(nombreUser=nombreUser, passwordUser=passwordUser, nroRutCli=selCliente)

        """ selUsuario = Usuario.objects.get(nroRutCli=selCliente)

        # Obteniendo y Enviando el nombre de usuario para acciones ha realizar en la página principal
        datosObtenidos = {
            'selUsuario': selUsuario
        }

    return render(request, 'core/index.html', datosObtenidos) """
    return redirect('index.html')

# Suscripción
def donarSuscripcion (request):
    return render(request,'core/donarSuscripcion.html')

# Cerrar Sesión
def cerrarSesión (request):
    return redirect('loginRegisterUser.html')

# Suscripción de Clientes registrados
def suscripcionUsuario (request):
    if request.method == 'POST':
        montoDonacion = request.POST['montoDonacion']
        nombreUser = request.POST['nombreUser']

        selUsuario = Usuario.objects.get(nombreUser=nombreUser)

        # Insertando al cliente identificado como Usuario Suscrito
        Suscrito.objects.create(nombreUser=selUsuario)

        """ messages.info(request, 'El usuario ha sido suscrito correctamente') """

    return redirect('index.html')

def desSuscripcion (request):
    if request.method == 'POST':
        nombreUser = request.POST['nombreUser']

        selUsuario = Suscrito.objects.get(nombreUser=nombreUser)

        # Eliminando al usuario identificado
        Suscrito.objects.filter(nombreUser=selUsuario).delete()

        """ datosObtenidos = {
            'nombreUser' : nombreUser
        }

    return render(request, 'core/index.html', datosObtenidos) """
    return redirect('index.html')

def listadoCompras (request):
    return render(request,'core/listadoCompras.html')

def obtenerDatosCompraProducto (request):
    if request.method == 'POST':
        idProducto = request.POST['idProducto']

        selProducto = Producto.objects.get(idProducto=idProducto)
    
    return render(request,'core/listadoCompras.html', selProducto)
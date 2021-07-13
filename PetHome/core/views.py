from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Venta, Cliente, Usuario, Suscrito

# Create your views here.
# Pagina Inicial
def index (request):
    # Mostrar los Productos a la Venta
    productos = Producto.objects.all()
    datosObtenidos = {
        'productos': productos
    }
    return render(request, 'core/index.html', datosObtenidos)

# Login de usuarios previamente registrados
def loginRegisterUser (request):
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
    return render(request, 'core/donarSuscripcion.html')

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

# Eliminación de Suscripción
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

# Página en la que se visualiza los productos seleccionados a comprar
def listadoCompras (request):
    return render(request,'core/listadoCompras.html')

# Obteniendo los datos del producto seleccionado
def obtenerDatosCompraProducto (request):
    if request.method == 'POST':
        idProducto = request.POST['idProducto']

        selProducto = Producto.objects.get(idProducto=idProducto)
        
        datosObtenidos = {
            'selProducto' : selProducto
        }

    return render(request, 'core/listadoCompras.html', datosObtenidos)

# MANTENEDORES
# Clientes
def mantenedorClientes (request):
    # Mostrar los Clientes registrados
    clientes = Cliente.objects.order_by("nroRutCli", "nombreCli")
    clientesObtenidos = {
        'clientes': clientes
    }

    return render(request, 'core/mantenedorClientes.html', clientesObtenidos)

def formAddClientes (request):
    return render(request, 'core/formAddClientes.html')

def addClientes (request):
    if request.method == 'POST':
        nroRutCli = request.POST['nroRutCli']
        dvRun = request.POST['dvRun']
        nombreCli = request.POST['nombreCli']
        apellidocli = request.POST['apellidocli']

        # Insertando al cliente identificado como Usuario Suscrito
        Cliente.objects.create(nroRutCli=nroRutCli,dvRun=dvRun,nombreCli=nombreCli,apellidocli=apellidocli)

    return redirect('mantenedorClientes.html')

def formUpdClientes (request):
    return render(request, 'core/formUpdClientes.html')

def updClientes (request):
    if request.method == 'POST':
        nroRutCli = request.POST['nroRutCli']
        nombreCli = request.POST['nombreCli']
        apellidocli = request.POST['apellidocli']
        
        selCliente = Cliente.objects.get(nroRutCli=nroRutCli)

        Cliente.objects.filter(nroRutCli=nroRutCli).update(nombreCli=nombreCli, apellidocli=apellidocli)

    return redirect('mantenedorClientes.html')
from django.shortcuts import render, redirect
from .models import Producto, Venta, Cliente, Usuario, Suscrito

# Create your views here.
# Pagina Inicial
def index(request):
    return render(request,'core/index.html')

# Login de usuarios previamente registrados
def loginRegisterUser(request):
    return render(request,'core/loginRegisterUser.html')

# Validación: Existe el usuario en la BD
def verificacionUser (request):
    if request.method == 'POST':
        username = request.POST['usernmaneCli']
        password = request.POST['passwordUser']

        selUsuario = Usuario.objects.get(nombreUser=username, passwordUser=password)

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

        return redirect('index.html')

# Suscriipción
def donarSuscripcion (request):
    return render(request,'core/donarSuscripcion.html')

class userObtenido:
            def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad
                super().__init__()

# Obteniendo el nombre del usuario para usarlo en caso de DonaciónSuscripción
def obtenerUser (request):
    nombreUser = userObtenido("Usuario", "16")
    contexto = {"nombreUser": nombreUser}
    return render(request, 'core/index.html', contexto)


# Cerrar Sesión
def cerrarSesión (request):
    messages = print("Your form was saved") 
    return redirect('loginRegisterUser.html')
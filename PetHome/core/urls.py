from django.urls import path 
from .views import index, loginRegisterUser, verificacionUser, registroUser, donarSuscripcion, cerrarSesión, suscripcionUsuario, desSuscripcion, listadoCompras, obtenerDatosCompraProducto, mantenedorClientes, formAddClientes

urlpatterns = [
    path('', loginRegisterUser, name="loginRegisterUser.html"),
    path('verificacionUser', verificacionUser, name="verificacionUser"),
    path('registroUser', registroUser, name="registroUser"),
    path('index/', index, name="index.html"),
    #path('obtenerUser', obtenerUser, name="obtenerUser"),
    path('index/donarSuscripcion/', donarSuscripcion, name="donarSuscripcion.html"),
    path('cerrarSesión', cerrarSesión, name="cerrarSesión"),
    path('suscripcionUsuario', suscripcionUsuario, name="suscripcionUsuario"),
    path('desSuscripcion', desSuscripcion, name="desSuscripcion"),
    path('listadoCompras/', listadoCompras, name="listadoCompras.html"),
    path('obtenerDatosCompraProducto', obtenerDatosCompraProducto, name="obtenerDatosCompraProducto"),
    path('mantenedorClientes/', mantenedorClientes, name="mantenedorClientes.html"),
    path('formAddClientes/', formAddClientes, name="formAddClientes.html"),
]
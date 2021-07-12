from django.urls import path 
from .views import index, loginRegisterUser, verificacionUser, registroUser, donarSuscripcion, cerrarSesión, suscripcionUsuario

urlpatterns = [
    path('', loginRegisterUser, name="loginRegisterUser.html"),
    path('verificacionUser', verificacionUser, name="verificacionUser"),
    path('registroUser', registroUser, name="registroUser"),
    path('index/', index, name="index.html"),
    #path('obtenerUser', obtenerUser, name="obtenerUser"),
    path('index/donarSuscripcion/', donarSuscripcion, name="donarSuscripcion.html"),
    path('cerrarSesión', cerrarSesión, name="cerrarSesión"),
    path('suscripcionUsuario', suscripcionUsuario, name="suscripcionUsuario"),
]
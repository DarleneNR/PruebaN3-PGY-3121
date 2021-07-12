from django.urls import path 
from .views import index, loginRegisterUser, verificacionUser, registroUser, donarSuscripcion, cerrarSesión

urlpatterns = [
    path('', loginRegisterUser, name="loginRegisterUser.html/"),
    path('verificacionUser', verificacionUser, name="verificacionUser"),
    path('registroUser', registroUser, name="registroUser"),
    path('index/', index, name="index.html/"),
    #path('obtenerUser', obtenerUser, name="obtenerUser"),
    path('donarSuscripcion/', donarSuscripcion, name="donarSuscripcion.html/"),
    path('cerrarSesión', cerrarSesión, name="cerrarSesión"),
]
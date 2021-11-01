from django.urls import path
from .views import UsuarioView, RegistrarUsuarioView, LoginConCredsView, ActualizarUsuarioView, LoginConTokenView
from knox.views import LogoutView, LoginView as KnoxLoginView

app_name = "usuarios"

urlpatterns = [
   path("usuario/<int:pk>", UsuarioView.as_view(), name="catalogo"),
   path("login/", LoginConCredsView.as_view(), name="login"),
   path("login-token", LoginConTokenView.as_view(), name="login-token"),
   path("registro/", RegistrarUsuarioView.as_view(), name="registro"),
   path("logout/", LogoutView.as_view(), name="logout"),
   path("actualizar/", ActualizarUsuarioView.as_view(), name="actualizar"),
]
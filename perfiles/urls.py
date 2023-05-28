from django.contrib import admin
from django.urls import path

from perfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView


urlpatterns = [
    # URLS Usuario y sesion
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    # URLS de Perfil
    path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
]
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'fec_nac', 'preferencias_string', 'favoritos_string')

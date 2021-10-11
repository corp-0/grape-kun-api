from django.contrib import admin
from .models import MangaPreview

# Register your models here.
@admin.register(MangaPreview)
class MangaPreviewAdmin(admin.ModelAdmin):
    fields = ( 'nombre', 'enlace_img', 'enlace_manga', 'generos', 'proveedor' )
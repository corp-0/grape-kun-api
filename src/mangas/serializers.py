from rest_framework import serializers
from .models import MangaPreview

class MangaPreviewSerializer(serializers.ModelSerializer):
    contenido_adulto = serializers.BooleanField()
    class Meta:
        model = MangaPreview
        fields = ( 'id', 'nombre', 'enlace_img', 'enlace_manga', 'generos_como_lista', 'generos', 'proveedor', 'contenido_adulto' )
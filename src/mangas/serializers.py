from rest_framework import serializers
from .models import MangaPreview

class MangaPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaPreview
        fields = ( 'id', 'nombre', 'enlace_img', 'enlace_manga', 'generos', 'proveedor' )

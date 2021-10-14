from rest_framework.generics import ListAPIView
from .models import MangaPreview
from .serializers import MangaPreviewSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from manga_scrap.modelos import MangaPreview as Preview, Genero
from manga_scrap.proveedores.mangaList import MangaList
import json

class MangaPreviewView(ListAPIView):
    queryset = MangaPreview.objects.all()
    serializer_class = MangaPreviewSerializer

class MangaDetalleView(APIView):
    def get(self, request, id=None):
        manga_list = MangaList()

        if id is None:
            return Response({"Error": "ID de consulta inválida"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            datos_preview = MangaPreview.objects.get(id=id)
        except MangaPreview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        generos = [Genero(g) for g in datos_preview.generos_como_lista]

        preview = Preview(
            nombre=datos_preview.nombre,
            enlace_imagen=datos_preview.enlace_img,
            enlace_manga=datos_preview.enlace_manga,
            generos=generos
        )

        respuesta = json.loads(manga_list.construir_manga(preview).to_json_string())
        return Response(respuesta, status=status.HTTP_200_OK)

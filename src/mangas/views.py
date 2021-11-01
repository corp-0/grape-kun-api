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
    """
    Vista para obtener una lista de mangas
    """
    queryset = MangaPreview.objects.all()
    serializer_class = MangaPreviewSerializer


class MangaDetalleView(APIView):
    """
    Vista para obtener el detalle de un manga.
    :param: id: id del manga
    :return: json con el detalle del manga
    """

    def get(self, request, id: int):
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
            generos=generos,
            contenido_adulto=datos_preview.contenido_adulto
        )

        respuesta = json.loads(manga_list.obtener_manga_detalle(preview).to_json_string())
        respuesta["manga_id"] = datos_preview.id
        return Response(respuesta, status=status.HTTP_200_OK)


class CapituloDetalleView(APIView):
    """
    Vista para obtener los datos de un capítulo.
    :param: id: id del capítulo
    :param: capitulo: índice del capítulo que pertenece a la vista de detalle.
    :return: json con los datos del capítulo, incluyendo sus imágenes
    """

    def get(self, request, id: int, capitulo: int):
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
            generos=generos,
            contenido_adulto=datos_preview.contenido_adulto
        )
        detalle = manga_list.obtener_manga_detalle(preview)
        try:
            capitulo = detalle.capitulos[capitulo]
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        respuesta = json.loads(manga_list.obtener_capitulo_detalle(capitulo.enlace).to_json_string())
        respuesta["manga_id"] = datos_preview.id
        return Response(respuesta, status=status.HTTP_200_OK)
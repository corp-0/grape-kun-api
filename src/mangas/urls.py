from django.urls import path
from .views import MangaPreviewView, MangaDetalleView, CapituloDetalleView, MangaPreviewAleatorioView

app_name = "mangas"

urlpatterns = [
   path("catalogo/", MangaPreviewView.as_view(), name="catalogo"),
   path("catalogo/<int:id>/", MangaDetalleView.as_view(), name="detalle"),
   path("catalogo/<int:id>/<int:capitulo>", CapituloDetalleView.as_view(), name="capitulo"),
   path("aleatorio/", MangaPreviewAleatorioView.as_view(), name="aleatorio"),
]
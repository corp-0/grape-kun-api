from django.urls import path
from .views import MangaPreviewView, MangaDetalleView

app_name = "mangas"

urlpatterns = [
   path("catalogo/", MangaPreviewView.as_view(), name="catalogo"),
   path("catalogo/<id>/", MangaDetalleView.as_view(), name="detalle")
]
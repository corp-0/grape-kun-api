from django.urls import path
from .views import MangaPreviewView

app_name = "mangas"

urlpatterns = [
   path("catalogo", MangaPreviewView.as_view(), name="catalogo")
]
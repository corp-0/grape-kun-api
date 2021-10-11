from django.core.management.base import BaseCommand
from mangas.models import MangaPreview, Proveedor
from manga_scrap.proveedores.mangaList import MangaList
import logging

log = logging.getLogger("grape-kun")

def limpiar_previews():
    Proveedor.objects.all().delete()
    MangaPreview.objects.all().delete()
    proveedor = Proveedor(nombre="MangaList")
    proveedor.save()

def generar_previews():
    manga_list = MangaList()
    catalogo = manga_list.generar_catalogo(1)
    for p in catalogo:
        log.info(f"Procesando: {p.nombre}")
        django_preview = MangaPreview(
            nombre=p.nombre,
            enlace_img=p.enlace_imagen,
            enlace_manga=p.enlace_manga,
            proveedor=Proveedor.objects.first()
        )
        django_preview.save()


class Command(BaseCommand):
    help = "Genera la indexación de manga previews"

    def handle(self, *args, **options):
        limpiar_previews()
        generar_previews()
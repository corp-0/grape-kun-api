from django.core.management.base import BaseCommand
from mangas.models import MangaPreview, Proveedor
from manga_scrap.proveedores.mangaList import MangaList
import logging

log = logging.getLogger("grape-kun")

def limpiar_previews():
    MangaPreview.objects.all().delete()
    Proveedor.objects.get_or_create(nombre="MangaList")

def generar_previews(paginas: int=None):
    manga_list = MangaList()
    log.info(f"Generando catálogo de {'total de ' if paginas is None else paginas} {'páginas' if paginas > 1 else 'página'}.")
    catalogo = manga_list.generar_catalogo(paginas)
    for p in catalogo:
        log.info(f"Procesando: {p.nombre}")
        django_preview = MangaPreview(
            nombre=p.nombre,
            enlace_img=p.enlace_imagen,
            enlace_manga=p.enlace_manga,
            proveedor=Proveedor.objects.first()
        )
        django_preview.agregar_generos([str(g) for g in p.generos])
        django_preview.save()

class Command(BaseCommand):
    help = "Genera la indexación de manga previews"
    def add_arguments(self, parser):
        parser.add_argument('--paginas', type=int)

    def handle(self, *args, **options):
        limpiar_previews()
        generar_previews(options.get('paginas'))
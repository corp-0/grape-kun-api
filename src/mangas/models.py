from django.db import models
from typing import List
from django.conf import settings

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)

class MangaPreview(models.Model):
    nombre = models.CharField(max_length=255)
    enlace_img = models.URLField()
    enlace_manga = models.URLField()
    generos = models.CharField(max_length=255, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def agregar_genero(self, genero: str) -> None:
        self.generos += f"{';'+genero if self.generos else genero}"

    def agregar_generos(self, generos: List[str]) -> None:
        for genero in generos:
            self.agregar_genero(genero)

    def remover_genero(self, genero: str) -> None:
        self.generos = (self.generos).replace(f";{genero}", "")

    @property
    def generos_como_lista(self) -> List[str]:
        return [g for g in (self.generos).split(";")]

    @property
    def contenido_adulto(self) -> bool:
        for genero in self.generos_como_lista:
            if genero.upper() in settings.GENEROS_ADULTOS:
                return True
        return False

    def a_json(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'enlace_img': self.enlace_img,
            'enlace_manga': self.enlace_manga,
            'generos': self.generos_como_lista,
            'proveedor': self.proveedor.nombre,
            'contenido_adulto': self.contenido_adulto
        }

    def __str__(self) -> str:
        return self.nombre

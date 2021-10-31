from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models
import json
from mangas.models import MangaPreview

class Usuario(AbstractUser):
    email = models.EmailField(verbose_name="Correo electronico", unique=True)
    username = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    fec_nac = models.DateTimeField(verbose_name="Fecha de nacimiento")
    favoritos_string = models.CharField(max_length=999999, verbose_name="Favoritos", default="[{}]")
    preferencias_string = models.JSONField(verbose_name="Preferencias", default=json.dumps(dict(filtrar_contenido_adulto=True, auto_login=True)))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def preferencias(self) -> dict:
        return json.loads(self.preferencias_string)
    
    @property
    def favoritos(self) -> List[MangaPreview]:
        mangas_favoritos = []
        mangas = json.loads(self.favoritos_string)
        for manga in mangas:
            mangas_favoritos.append(MangaPreview.objects.get(id=manga.get("id")).a_json())

        return mangas_favoritos

    def __str__(self):
        return self.username

from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)

class Genero(models.Model):
    nombre = models.CharField(max_length=25)

class MangaPreview(models.Model):
    nombre = models.CharField(max_length=255)
    enlace_img = models.URLField()
    enlace_manga = models.URLField()
    generos = models.ManyToManyField(Genero)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Manga(models.Model):
    preview = models.OneToOneField(MangaPreview, on_delete=models.CASCADE)

class Capitulo(models.Model):
    nombre = models.CharField(max_length=255)
    enlace = models.URLField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

class Imagen(models.Model):
    url = models.URLField()
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)


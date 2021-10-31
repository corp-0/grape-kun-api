from django.core.management.base import BaseCommand
from datetime import datetime

from usuarios.models import Usuario


class Command(BaseCommand):
    help = "Crea un nuevo usuario administrativo para el sitema"

    def handle(self, *args, **options):
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        email = input("Ingrese el email: ")
        fec_nac = datetime.now()

        usuario = Usuario.objects.create(
            username=username,
            email=email,
            fec_nac=fec_nac
        )

        usuario.set_password(password)
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.save()
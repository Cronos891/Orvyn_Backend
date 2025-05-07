from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Creates a superuser with predefined credentials'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando proceso de creación de superusuario...'))
        User = get_user_model()
        username = 'Cronos891'
        email = 'rars2303@gmail.com'
        password = 'Cronos18847489'

        try:
            # Intentar eliminar el usuario si ya existe
            User.objects.filter(username=username).delete()
            self.stdout.write(self.style.NOTICE(f'Eliminando usuario existente {username} si existe...'))

            # Crear nuevo superusuario
            self.stdout.write(self.style.NOTICE('Creando nuevo superusuario...'))
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado exitosamente'))

            # Verificación adicional
            if User.objects.filter(username=username, is_superuser=True).exists():
                self.stdout.write(self.style.SUCCESS(f'Verificado: El superusuario "{username}" existe y tiene permisos correctos'))
            else:
                self.stdout.write(self.style.ERROR(f'Error: El usuario "{username}" no existe o no tiene permisos de superusuario'))

        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Error de integridad al crear el superusuario: {str(e)}'))
            raise
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error inesperado: {str(e)}'))
            self.stdout.write(self.style.ERROR(f'Tipo de error: {type(e).__name__}'))
            raise
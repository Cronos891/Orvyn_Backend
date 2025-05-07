from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando proceso de creación de superusuario...'))
        User = get_user_model()
        try:
            self.stdout.write('Verificando si existe un superusuario...')
            if not User.objects.filter(is_superuser=True).exists():
                self.stdout.write('No se encontró superusuario. Creando uno nuevo...')
                User.objects.create_superuser(
                    username='Cronos891',
                    email='rars2303@gmail.com',
                    password='Cronos18847489'
                )
                self.stdout.write(self.style.SUCCESS('¡Superusuario creado exitosamente con username: Cronos891!'))
            else:
                existing_user = User.objects.filter(is_superuser=True).first()
                self.stdout.write(
                    self.style.WARNING(f'Ya existe un superusuario con username: {existing_user.username}')
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al crear superusuario: {str(e)}'))
            self.stdout.write(self.style.ERROR('Detalles del error:'))
            self.stdout.write(self.style.ERROR(f'Tipo de error: {type(e).__name__}'))
            self.stdout.write(self.style.ERROR(f'Mensaje completo: {str(e)}'))
            raise
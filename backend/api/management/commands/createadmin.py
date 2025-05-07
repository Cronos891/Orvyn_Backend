from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username='Cronos891',
                    email='rars2303@gmail.com',
                    password='Cronos18847489'
                )
                self.stdout.write(self.style.SUCCESS('Superuser created successfully with username: Cronos891'))
            else:
                existing_user = User.objects.filter(is_superuser=True).first()
                self.stdout.write(
                    self.style.WARNING(f'Superuser already exists with username: {existing_user.username}')
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {str(e)}'))
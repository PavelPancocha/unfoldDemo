from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.factories import OrgFactory, CarFactory

class Command(BaseCommand):
    help = 'Create demo data for the application'

    def handle(self, *args, **options):
        # Create 2 Orgs
        OrgFactory.create_batch(2)

        # Create 4 Cars with assigned Orgs and Owners
        CarFactory.create_batch(4)

        # Create superuser if not already exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))

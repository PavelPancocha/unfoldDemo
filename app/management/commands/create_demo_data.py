from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app.factories import CarFactory, OrgFactory


class Command(BaseCommand):
    help = 'Create demo data for the application'

    def handle(self, *args, **options):
        # Create 2 Orgs
        orgs = OrgFactory.create_batch(3)
        self.stdout.write(self.style.SUCCESS('Orgs created'))

        # Create 4 Cars with assigned Orgs and Owners
        for org in orgs:
            CarFactory.create_batch(5, org=org)
        self.stdout.write(self.style.SUCCESS('Cars created'))

        # Create superuser if not already exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))

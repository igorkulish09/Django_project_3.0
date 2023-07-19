from django.core.management.base import BaseCommand
from magazine.models import Model1, Model2


class Command(BaseCommand):
    help = 'Populates the database with a large amount of data'

    def handle(self, *args, **options):
        for i in range(100):
            Model1.objects.create(name=f'Model1_{i}')
        for i in range(200):
            Model2.objects.create(name=f'Model2_{i}')

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))

from django.core.management.base import BaseCommand
from faker import Faker
from faker_music import MusicProvider

from shop.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('¡Hola, usuario!')

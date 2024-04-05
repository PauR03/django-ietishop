from django.core.management.base import BaseCommand
from faker import Faker
from faker_music import MusicProvider
from random import randint

from shop.models import *

faker = Faker(["es_CA","es_ES"])

class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'
    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(MusicProvider)
        
        CANTIDAD_CATEGORIAS = 4
        contador = 0
        while CANTIDAD_CATEGORIAS > 0:
            categoria = Categoria()
            newObject = fake.music_instrument_object()
            newCategoria = newObject["category"]

            # Evitar bucle infinito
            if contador == 100:
                break
            contador += 1

            # Si existe la categoria en la base de datos, no la añade
            if Categoria.objects.filter(nom=newCategoria).exists():
                continue
            print("Categoria: " + newCategoria)
            categoria.nom = newCategoria
            categoria.save()

            for newInstrument in newObject["instruments"]:
                producte = Producte()
                producte.nom = newInstrument
                producte.descripcio = "Lorem"
                producte.preu = randint(10, 100)
                producte.categoria = categoria
                producte.quantitat_disponible = randint(1, 100)
                producte.save()
                print("Producte: " + newInstrument)
            CANTIDAD_CATEGORIAS -= 1

        self.stdout.write('Productos añadidos correctamente')

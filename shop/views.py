from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def product_list(request):
    productes = Producte.objects.all()
    categories = Categoria.objects.all()
    return render(request, "product_list.html", {"productes": productes, "categories": categories})

def car(request):
    return render(request, "car.html")

# def product_list_cat(request, id_cat):
#     productes = Producte.objects.filter(categoria=id_cat)
#     return render(request, "product_list.html", {"productes": productes})
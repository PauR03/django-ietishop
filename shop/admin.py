from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Producte)
admin.site.register(Compra)
admin.site.register(DetallCompra)
admin.site.register(Cistella)

class ProducteInline(admin.TabularInline):
    model = Producte
    readonly_fields = ["descripcio"]

class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 0
    exclude = ("descripcio",)

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaInline, ProducteInline]
    list_display = ["nom","parent"]

admin.site.register(Categoria, CategoriaAdmin)
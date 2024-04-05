from . import views
from django.urls import path

# Create your views here.
urlpatterns = [
    path("", views.product_list),
    path("cat/<id_cat>", views.product_list_cat),
]
from . import views, api
from django.urls import path

# Create your views here.
urlpatterns = [
    path("", views.product_list),
    path("car/", views.car),
    # path("cat/<id_cat>", views.product_list_cat),
    path("api/prods", api.getProducts),
    path("api/prods/<int:id_cat>", api.getProductsByCategory),
    path("api/payment", api.makePayment),
]
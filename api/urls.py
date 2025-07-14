from django.urls import path
from .views import get_products, AllProducts


urlpatterns = [
    path("items/", AllProducts.as_view(), name="get_products"),
    path("products/", get_products, name="get_products"),
]
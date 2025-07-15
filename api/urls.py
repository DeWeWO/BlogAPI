from django.urls import path
from .views import get_cats


urlpatterns = [
    path("cats/", get_cats, name="get_cats"),
]
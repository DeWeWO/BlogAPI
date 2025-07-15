from django.urls import path
from .views import get_cats, create_cat


urlpatterns = [
    path("cats/", get_cats, name="get_cats"),
    path("create/cat/", create_cat, name="create_cat")
]
from django.urls import path
from .views import get_cats, create_cat, detail_cat, PostListAPIView, PostCreateAPIView


urlpatterns = [
    path("cats/", get_cats, name="get_cats"),
    path("create/cat/", create_cat, name="create_cat"),
    path("cat/<slug:slug>/", detail_cat, name="detail_cat"),
    # Posts urls
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("create/post/", PostCreateAPIView.as_view(), name="post-create"),
]
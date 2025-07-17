from django.urls import path
from .views import get_cats, create_cat, detail_cat, PostListAPIView, PostCreateAPIView, PostRetrieveUpdateDestroyAPIView, PostListCreateAPIView, PostRetriveUpdateDestroyAPIView2
from .auth.sign_up import RegisterAPIView
from .auth.sign_in import LoginAPIView
from .auth.sign_out import LogOutAPIView


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogOutAPIView.as_view(), name="logout"),
    path("cats/", get_cats, name="get_cats"),
    path("create/cat/", create_cat, name="create_cat"),
    path("cat/<slug:slug>/", detail_cat, name="detail_cat"),
    # Posts urls
    path("posts/", PostListCreateAPIView.as_view(), name="post-list"),
    path("create/post/", PostCreateAPIView.as_view(), name="post-create"),
    path("post/<slug:slug>/", PostRetriveUpdateDestroyAPIView2.as_view(), name="post-detail") 
]
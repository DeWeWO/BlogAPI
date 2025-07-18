from django.urls import path
from .views import get_cats, create_cat, detail_cat, PostListAPIView, PostCreateAPIView, PostRetrieveUpdateDestroyAPIView, PostRetriveUpdateDestroyAPIView2, PostListViewSet # PostListCreateAPIView
from .auth.sign_up import RegisterAPIView
from .auth.sign_in import LoginAPIView
from .auth.sign_out import LogOutAPIView
from rest_framework.routers import DefaultRouter, SimpleRouter


router = SimpleRouter()
router.register("post", PostListViewSet)

post_list = PostListViewSet.as_view({"get": "list"})
post_create = PostListViewSet.as_view({"post": "create"})


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogOutAPIView.as_view(), name="logout"),
    path("cats/", get_cats, name="get_cats"),
    path("create/cat/", create_cat, name="create_cat"),
    path("cat/<slug:slug>/", detail_cat, name="detail_cat"),
    # Posts urls
    # path("posts/", PostListCreateAPIView.as_view(), name="post-list"),
    # path("create/post/", PostCreateAPIView.as_view(), name="post-create"),
    # path("post/<slug:slug>/", PostRetriveUpdateDestroyAPIView2.as_view(), name="post-detail"),
    post_list,
    post_create,
]

urlpatterns += router.urls
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes  # FBV (Function Based View)
from rest_framework.views import APIView #CBV (Class Based View)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ViewSet


@api_view(["GET"])
@permission_classes([AllowAny])
def get_cats(request: Request):
    cats = Category.objects.all()
    serializer = CategorySerializer(cats, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_cat(requuest: Request):
    if requuest.method == "POST":
        serializer = CategorySerializer(data=requuest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def detail_cat(request: Request, slug: str):
    category = get_object_or_404(Category, slug=slug)
    if request.method == "GET":
        return Response(data=CategorySerializer(instance=category).data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "PATCH":
    #     serializer = CategorySerializer(instance=category, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        category.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostCreateAPIView(GenericAPIView):
    serializer_class = PostSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class PostRetrieveUpdateDestroyAPIView(GenericAPIView):
    serializer_class = PostSerializer
    lookup_field = "slug"
    queryset = Post.objects.all()
    
    def get(self, request, slug):
        product = self.get_object()
        serializer = PostSerializer(instance=product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        product = self.get_object()
        serializer = PostSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, slug):
        product = self.get_object()
        product.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)



# class PostListCreateAPIView(ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all().order_by("id")
#     permission_classes = (IsAuthenticated, )
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['category', 'author']
#     search_fields = ['author__username', 'title', 'description']
#     ordering_fields = ['author', 'category']
    
#     def get_queryset(self):
#         username = self.request.query_params.get("username")
#         if username is not None:
#             return Post.objects.filter(author__username=username)
#         return super().get_queryset()

class PostListViewSet(ViewSet):
    queryset = Post.objects.all()
    
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status.HTTP_201_CREATED)

class PostRetriveUpdateDestroyAPIView2(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"

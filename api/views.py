from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view # FBV (Function Based View)
from rest_framework.views import APIView #CBV (Class Based View)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET"])
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
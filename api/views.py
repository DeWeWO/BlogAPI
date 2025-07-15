from django.shortcuts import render
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
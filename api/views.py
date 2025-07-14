from django.shortcuts import render
from rest_framework.decorators import api_view # FBV
from rest_framework.views import APIView #CBV
from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

data = [
    {
        "name": "iPhone",
        "price": 1300
    },
    {
        "name": "Samsung",
        "price": 1000
    },
    {
        "name": "Vivo",
        "price": 300
    }
]

# FBV(Function Based View)
@api_view(http_method_names=["GET", "POST"])
def get_products(request: Request):
    if request.method == "POST":
        print(request.data)
    return Response(data=data)


# CBV(Class Based View)
class AllProducts(APIView):
    def get(self, request):
        print(request)
        return Response(data={"items": [{"name": "Test"}]}, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        return Response(data=request.data, status=status.HTTP_201_CREATED)
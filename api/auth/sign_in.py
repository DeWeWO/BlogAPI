from api.serializers import LoginSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response(data={"token": token.key}, status=status.HTTP_201_CREATED)

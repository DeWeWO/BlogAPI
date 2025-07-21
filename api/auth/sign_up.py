from api.serializers import RegisterSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

class RegisterAPIView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = RegisterSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)



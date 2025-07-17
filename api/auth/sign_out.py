from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class LogOutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response(data={"success": "Logged Out!"}, status=status.HTTP_200_OK)
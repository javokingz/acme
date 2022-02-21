from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response

from users.api.serializer import UserRegisterSerializer


class RegisterView(APIView):
    """Registro de los usuarios"""

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
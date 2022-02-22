"""Vistas para el usuario"""
from urllib import request, response
from rest_framework import status 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializer import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User


class RegisterView(APIView):
    """Registro de los usuarios"""

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    """Traer y actualizar uasuarios"""
    permission_classes = [IsAuthenticated]


    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error, status.HTTP_400_BAD_RESQUEST)
        
       
"""Serializadores del api de Users"""
from rest_framework import  serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'saldo']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """Retorna los datos del usuario"""
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'saldo']

class UserUpdateSerializer(serializers.ModelSerializer):
    """Actualiza los datos del usuario"""
    class Meta:
        model = User
        fields= ['first_name', 'last_name']

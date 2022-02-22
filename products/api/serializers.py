from rest_framework import serializers
from products.models import Product
from users.api.serializer import UserSerializer
from categories.api.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']


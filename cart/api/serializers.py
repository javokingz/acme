from rest_framework import serializers
from cart.models import Cart
from products.api.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ['id', 'products', 'buyer']
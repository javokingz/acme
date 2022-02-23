from rest_framework.serializers import ModelSerializer
from cart.models import Cart
from products.api.serializers import ProductSerializer

class CartSerializer(ModelSerializer):
    #product = ProductSerializer(read_only=True, many=True)

    class Meta:
        model=Cart
        
        fields = ['id', 'product', 'total_moun', 'user']
from rest_framework import serializers

from orders.models import Order
from products.api.serializers import ProductSerializer
from products.models import Product
from users.api.serializer import UserSerializer






class OrderSerializer(serializers.ModelSerializer):

    """Serializer for the Order model."""
    #customer = UserSerializer(read_only=True)
    # used to represent the target of the relationship using its __unicode__ method
    
    class Meta:
        model = Order
        fields = ('id', 'customer', 'product', 'total','quantity', 'created_at', 'updated_at')

    def create(self, validated_data):
        """Override the creation of Order objects
        Parameters
        ----------
        validated_data: dict
        """
        order = Order.objects.create(**validated_data)
        return order

class CheckoutSerializer(serializers.ModelSerializer):

    model= Order
    fields = ['customer', 'ptoduct', 'total', 'quantity']
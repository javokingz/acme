from __future__ import unicode_literals
from django.db.models import FloatField
from django.db.models import F
from django.db.models import Sum

from django.db.models import FloatField

from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import User
from orders.models import Order
from products.models import Product
from orders.api.serializers import OrderSerializer, CheckoutSerializer
from products.api.serializers import ProductSerializer
import pickle

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or created.
    
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def put(self, request, *args, **kwargs):
        order = Order.objects.get(id=request.order.id)
        #data = request.data

        order.total= 700
        order.save()

        print(order.total)
        serializer = CheckoutSerializer(order)
        
        
        return Response(serializer)


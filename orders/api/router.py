from rest_framework.routers import DefaultRouter
from orders.api.views import OrderViewSet
from rest_framework import routers
from . import views
from django.urls import include, path



router_order = DefaultRouter()
router_order.register(prefix='order', basename='order', viewset=OrderViewSet)
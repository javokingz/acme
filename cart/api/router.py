from rest_framework.routers import DefaultRouter
from cart.api.views import CartApiViewSet
from rest_framework import routers
from . import views
from django.urls import include, path


router_cart = routers.DefaultRouter()
router_cart.register(r'cart', views.CartApiViewSet)
#router_cart.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include((router_cart.urls, 'cart'))),
]
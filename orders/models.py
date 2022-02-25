from django.db import models
from tiendaAcme import settings
from django.db.models import SET_NULL
from products.models import Product

class Order(models.Model):
  
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='customer', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







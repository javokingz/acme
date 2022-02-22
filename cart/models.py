from django.db import models
from users.models import User
from products.models import Product
from django.db.models import SET_NULL


class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    


from django.db import models
from users.models import User
from products.models import Product
from django.db.models import SET_NULL



class ShCart(models.Model):
   
    customer = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
   
    cart = models.ForeignKey(ShCart, related_name='items',on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.product.name, self.quantity)

class Order(models.Model):
    """
    An Order is the more permanent counterpart of the shopping cart. It represents
    the frozen the state of the cart on the moment of a purchase. In other words,
    an order is a customer purchase.
    """
    customer = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE,null=True, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    """A model that contains data for an item in an order."""
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.product.name, self.quantity)





# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     quantity = models.PositiveIntegerField(default=1)
#     total_moun = models.PositiveIntegerField(default=1)
#     created = models.DateTimeField(auto_now_add=True)

 
    
    


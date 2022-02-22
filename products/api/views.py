from rest_framework.viewsets import ModelViewSet
from products.models import Product
from products.api.serializers import ProductSerializer
#from products.api.permissions import IsAdminOrNot


class ProductApiViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'name'
from cgitb import lookup
from rest_framework.viewsets import ModelViewSet
#from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrNot

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrNot]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
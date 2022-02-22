from rest_framework.viewsets import ModelViewSet
#from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
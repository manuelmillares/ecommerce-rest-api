from rest_framework import viewsets
from product import serializers
from ecommerce_api import models


class ProductViewSet(viewsets.ModelViewSet):
    """Handle creating listing and updating products"""
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

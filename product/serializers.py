from rest_framework import serializers
from ecommerce_api import models


class ProductSerializer(serializers.ModelSerializer):
    """Serializes a product object"""

    class Meta:
        model = models.Product
        fields = ('id', 'title', 'description', 'price')

# from django.shortcuts import render
from ecommerce_api import serializers
from ecommerce_api import models
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

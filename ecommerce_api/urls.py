from django.urls import path, include
from ecommerce_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]

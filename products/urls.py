from django.urls import path
from .views import get_products, search

urlpatterns = [
    path('', get_products, name='get_products'),
    path('', search , name='search'),
]
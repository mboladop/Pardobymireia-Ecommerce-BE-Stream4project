from django.urls import path
from .views import see_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('see/', see_cart, name ='see_cart'),
    path('add/', add_to_cart, name ='add_to_cart'),
    path('remove/', remove_from_cart, name = 'remove_from_cart')
]
from django.urls import path
from django.conf.urls import include, url
from .views import get_products, search, category_detail, product_profile

urlpatterns = [
    path('<pk>/', category_detail, name='category_detail'),
    path('', get_products, name='get_products'),
    path('profile/<pk>/', product_profile, name='product_profile'),
    # path('', search , name='search'),
]
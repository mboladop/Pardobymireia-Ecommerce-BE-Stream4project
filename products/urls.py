from django.urls import path
from django.conf.urls import include, url
from .views import get_products, search, category_detail

urlpatterns = [
    path('<pk>/', category_detail, name='category_detail'),
    path('', get_products, name='get_products'),
    # path('', search , name='search'),
]
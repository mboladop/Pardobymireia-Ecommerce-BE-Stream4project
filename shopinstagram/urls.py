from django.urls import path
from django.conf.urls import include, url
from .views import shopinstagram

urlpatterns = [
    path('', shopinstagram, name='shopinstagram')
]
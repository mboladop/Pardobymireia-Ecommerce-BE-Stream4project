from django.urls import path
from django.conf.urls import include, url
from .views import home, novedades
from blog.views import get_blogs

urlpatterns = [
    path('', home, name='home'),
    path('novedades/', novedades, name='novedades'),
    # path('', search , name='search'),
]
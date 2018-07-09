from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from accounts import urls as accounts_urls
from accounts.views import get_index
from products import urls as products_urls
from products.views import get_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    #path('', include(posts_urls)),
    #path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
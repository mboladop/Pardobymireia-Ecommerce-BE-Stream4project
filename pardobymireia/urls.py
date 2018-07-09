from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from accounts import urls as accounts_urls
from accounts.views import get_index
from products import urls as products_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name = 'home'),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('blog/', include(blog_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
] 
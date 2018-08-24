from django.contrib import admin
from django.contrib.auth import views as auth_views
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
from home import urls as home_urls
from shopinstagram import urls as shopinstagram_urls
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', get_index, name = 'index'),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('blog/', include(blog_urls)),
    path('', include(home_urls), name = 'index'),
    path('shopinstagram/', include(shopinstagram_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
] 
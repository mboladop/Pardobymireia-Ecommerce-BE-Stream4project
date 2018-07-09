from django.urls import path
from blog.views import get_blogs, blog_detail, new_blog, edit_blog, liked_blogs

urlpatterns = [
    path('new/', new_blog, name='new_blog'),
    path('<pk>/edit', edit_blog, name='edit_blog'),
    path('<pk>/', blog_detail, name='blog_detail'),
    path('', get_blogs, name='get_blogs'),
    path('', liked_blogs, name='liked_blogs'),
]
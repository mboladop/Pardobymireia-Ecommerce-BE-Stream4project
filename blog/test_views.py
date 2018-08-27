from django.test import TestCase
from .models import Blog
from .forms import BlogPostForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages



class TestBlogViews(TestCase):
    def test_get_blogs(self):
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
    
    def test_view_blog_detail(self):
        blog = Blog.objects.create(title='Test Discussion Blog', content='Test Discussion Blog Content')
        self.assertEqual(Blog.objects.count(), 1)
        response = self.client.get("/blog/1/".format(blog.pk))
        self.assertEqual(response.status_code, 200)
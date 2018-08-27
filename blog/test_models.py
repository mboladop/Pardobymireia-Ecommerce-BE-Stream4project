from django.test import TestCase
from .models import Blog
from django.contrib.auth.models import User

class TestBlogModel(TestCase):

    def test_create_blog(self):
        blog = Blog(content='Some test content.')
        blog.save()
        self.assertEqual(blog.content, "Some test content.")
        self.assertFalse(blog.title)


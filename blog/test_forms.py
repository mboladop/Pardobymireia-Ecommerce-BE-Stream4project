from django.test import TestCase
from .forms import BlogPostForm
from .models import Blog

# Create your tests here.

class TestBlogPostForms(TestCase):              
    def test_blog_content(self):
        form = BlogPostForm({'Title':'Title'})
        self.assertFalse(form.is_valid())
        print(form.errors['content'], ['This field is required.'])


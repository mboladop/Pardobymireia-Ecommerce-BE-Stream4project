from django.apps import apps
from django.test import TestCase
from .apps import BlogConfig


class TestblogConfig(TestCase):

    def test_blog_app(self):
        self.assertEqual("blog", BlogConfig.name)
        self.assertEqual("blog", apps.get_app_config("blog").name)
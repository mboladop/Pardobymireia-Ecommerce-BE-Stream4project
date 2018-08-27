from django.test import TestCase
from django.apps import apps
from .apps import ShopinstagramConfig

class TestShopinstagramConfig(TestCase):

    def test_shopinstagram_app(self):
        self.assertEqual("shopinstagram", ShopinstagramConfig.name)
        self.assertEqual("shopinstagram", apps.get_app_config("shopinstagram").name)
        
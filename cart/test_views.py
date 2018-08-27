from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
from django.urls import reverse


class TestCartViews(TestCase):

    def test_see_cart(self):
        page = self.client.get("/cart/see/")
        self.assertEqual(page.status_code, 200)

    

from django.test import TestCase
from .models import Product, Category
from django.contrib.auth.models import User

class TestProductViews(TestCase):

    def test_get_product(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)

    
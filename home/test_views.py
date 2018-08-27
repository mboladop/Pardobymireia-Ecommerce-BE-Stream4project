from django.test import TestCase
from django.contrib.auth.models import User

class TestViews(TestCase):

    def test_get_home(self):
        self.client.login(username='user1', password='password1')
        page = self.client.get("")
        self.assertEqual(page.status_code, 200)

    def test_get_novedades(self):
        self.client.login(username='user1', password='password1')
        page = self.client.get("/novedades/")
        self.assertEqual(page.status_code, 200)

    
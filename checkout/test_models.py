from django.test import TestCase
from .models import Order, OrderLineItem


class TestCheckoutModels(TestCase):

    def test_place_order(self):
        order = Order(full_name='Mireia Istired', phone_number="7778254",
                      country='Spain', postcode='11111')
        order.save()
        self.assertEqual(order.full_name, "Mireia Istired")
        self.assertEqual(order.phone_number, "7778254")
        self.assertEqual(order.country, 'Spain')
        self.assertEqual(order.postcode, '11111')
        self.assertFalse(order.county)
        self.assertFalse(order.town_or_city)
        self.assertFalse(order.street_address_1)
        self.assertFalse(order.street_address_2)

    def test_place_order_products(self):
        order_line_item = OrderLineItem()
        self.assertFalse(order_line_item.quantity)

from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_items = []
    total = 0
    
    for p in cart:
           product = get_object_or_404(Product, pk=p)
           cart_item = {
               'product': product, 
               'quantity': cart[p],
               'sub_total': cart[p]*product.price
           }
           # products.append((phone, cart[p])
           cart_items.append(cart_item)
           total += cart_item['sub_total']

    return {'cart_items': cart_items, 'total': total}
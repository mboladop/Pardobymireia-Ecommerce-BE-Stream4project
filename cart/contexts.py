from .utils import get_cart_items_and_total

def get_total_cart_items(request):
    cart = request.session.get('cart', {})
    total_cart_items = len(get_cart_items_and_total(cart)['cart_items'])
    return {'total_cart_items': total_cart_items}
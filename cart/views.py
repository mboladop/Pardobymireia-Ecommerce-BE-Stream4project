from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product
from .utils import get_cart_items_and_total
# Create your views here.
def see_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    return render(request, "cart/yourcart.html", context)
    
def add_to_cart(request):   
    # Get the product we're adding
    id = request.POST['product_id']
    product = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart = request.session.get('cart', {})

    # Update the Cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return redirect('get_products')
    
def remove_from_cart(request):
     id = request.POST['product_id']
     #product = get_object_or_404(Product, pk=id)
     cart = request.session.get('cart', {})
     if id in cart: 
         cart[id]-=1
         if cart[id]==0:
             del cart[id]
     request.session['cart'] = cart
     return  redirect('see_cart')
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse



# Create your views here.
def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})
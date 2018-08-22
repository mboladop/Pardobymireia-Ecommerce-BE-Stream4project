from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, Category
from django.http import HttpResponse



# Create your views here.

def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})

def category_detail(request, pk):
    products = get_list_or_404(Product, category=pk)
    return render(request, 'products/products.html', {"products": products, "current": int(pk)})


def product_profile(request, pk):
    """
    Create a view that returns a single
    product object based on the item ID (pk) and
    render it to the 'product_profile.html' template.
    Or return a 404 error if the product is
    not found
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_profile.html", {'product': product})


def search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/products.html", {"products": products})


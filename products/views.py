from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, Category
from django.http import HttpResponse



# Create your views here.
def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})
    
def search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/products.html", {"products": products})

def category_detail(request, pk):
    products = get_list_or_404(Product, category=pk)
    return render(request, 'products/products.html', {"products": products, "current": int(pk)})
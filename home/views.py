from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def novedades(request):
    return render(request, "home/novedades.html")

def get_blogs(request):
    blogs = Blog.objects.all()
    
    return render(request, "blog/blog.html", {'blogs': blogs})
    
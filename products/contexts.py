from django.shortcuts import get_list_or_404
from .models import Category

def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories }
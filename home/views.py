from django.shortcuts import render
from products.models import Product, Brand
from .models import Baner

# Create your views here.


def home(request):
    feature_products = Product.objects.filter(flag="Freature")[:6]
    new_products = Product.objects.filter(flag="New")[:6]
    return render(request, 'home.html', {'products':feature_products})
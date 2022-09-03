from django.shortcuts import render
from django.views.generic import ListView
from .models import product

class ProductList(ListView):
    model = product



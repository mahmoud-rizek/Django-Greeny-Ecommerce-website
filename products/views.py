from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import product

class ProductList(ListView):
    model = product

class ProductDetail(DetailView):
    model = product

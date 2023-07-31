from django.shortcuts import render
from products.models import Product, Brand, Category, productReviews
from .models import Baner
from django.db.models import Count
# Create your views here.


def home(request):
    feature_products = Product.objects.filter(flag="Feature")[:6]
    new_products = Product.objects.filter(flag="New")[:6]
    sal_products = Product.objects.filter(flag="Sale")[:10]
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    catefories = Category.objects.all().annotate(product_count=Count('product_category'))
    reviews = productReviews.objects.all()
    return render(request, 'home.html', {'feat_products':feature_products,
    'new_product':new_products,
    'sal_products':sal_products,
    'brands':brands,
    'category':catefories,
    'productReviews':reviews})
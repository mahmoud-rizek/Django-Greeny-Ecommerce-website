from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import product, productImages, Brand, Category
from django.db.models import Count, Q


def testing_page(request):
    # objects = product.objects.all()  # select all products
    # objects = product.objects.filter(price__range=(120, 400))
    # objects = product.objects.filter(name__contains='sara')
    # objects = product.objects.filter(name__startswith='ma', price__gt=490)
    objects = product.objects.filter(
        Q(name__startswith='ma') |
        Q(price__gt=490))

    return render(request, "products/testing.html", {"products": objects})


class ProductList(ListView):
    model = product
    paginate_by = 250


class ProductDetail(DetailView):
    model = product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = productImages.objects.filter(product=myproduct)
        context["related"] = product.objects.filter(
            category=myproduct.category)[:10]
        return context


class BrandList(ListView):
    model = Brand
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().annotate(
            product_count=Count('product_brand'))
        return context


class BrandtDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countcontext = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brands"] = Brand.objects.all().annotate(
            product_count=Count('product_brand'))

        context["brand_products"] = product.objects.filter(brand=brand)
        return context


class CategoryList(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all().annotate(
            product_count=Count('product_category'))
        return context

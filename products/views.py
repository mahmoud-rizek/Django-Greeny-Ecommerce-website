from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import product, productImages, Brand, Category
from django.db.models import Count, Q , F


def testing_page(request):
    # objects = product.objects.all()  # select all products

            ## Filter by colum
            
    # objects = product.objects.filter(price__range=(110, 122)) 
    
    # objects = product.objects.filter(category__id=33)
    # objects = product.objects.filter(category__id__gt=30)

    # objects = product.objects.filter(name__contains='sara')# filter by name
    # objects = product.objects.filter(name__startswith='ma', price__gt=490)
    # objects = product.objects.filter(name__endswith='a')

    # objects = product.objects.filter(desc__isnull=True)
    # objects = product.objects.filter(quantity__gt=10)


            # _________ Q ________________

    # objects = product.objects.filter(
    #     Q(name__startswith='ma') | # select this or this
    #     Q(price__gt=490)
    # )

    # objects = product.objects.filter(
    #     Q(name__startswith='ma') & #select this and this
    #     Q(price__gt=490)
    # # )

    # objects = product.objects.filter(
    #     Q(name__startswith='ma') & #select this and not this
    #     ~Q(price__gt=490)
    # )

    # # objects = product.objects.filter(quantity=F('category__id')) # Refrance keys

            # _________ Order by ________________

    # objects = product.objects.order_by('name')  # ترتيب تصاعدي 
    # objects = product.objects.order_by('-name') # ترتيب تنازلي    
    # objects = product.objects.filter(quantity=F('category__id')).order_by('name')[:10]


    # objects = product.objects.earliest('name')
    # objects = product.objects.latest('name')
    # objects = product.objects.values('id', 'name')
    # objects = product.objects.values_list('id', 'name')
    objects = product.objects.only('id', 'name')

    
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

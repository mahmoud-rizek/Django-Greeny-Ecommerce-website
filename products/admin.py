from django.contrib import admin
from .models import Product, productImages, Category, productReviews, Brand
# Register your models here.


class productImagesInline(admin.TabularInline):
    model = productImages


class productadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'flag']
    inlines = [productImagesInline]

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','id']



admin.site.register(Product, productadmin)
admin.site.register(productImages)
admin.site.register(productReviews)
admin.site.register(Category, categoryadmin)
admin.site.register(Brand, categoryadmin)
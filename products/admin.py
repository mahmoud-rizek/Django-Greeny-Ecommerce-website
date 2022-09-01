from django.contrib import admin
from .models import product, productImages, Category, productReviews, Brand
# Register your models here.

class productadmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'flag']


admin.site.register(product, productadmin)
admin.site.register(productImages)
admin.site.register(productReviews)
admin.site.register(Category)
admin.site.register(Brand)
from django.shortcuts import render

from django.contrib.auth.models import User
from products import models as product_models
from orders import models as order_models
# Create your views here.


from .tasks import print_wellcome

def welcome(request):
    print_wellcome(10)
    

def dashboard(request):
    users = User.objects.all().count()
    products = product_models.product.objects.all().count()
    reviews = product_models.productReviews.objects.all().count()
    categories = product_models.Category.objects.all().count()
    brands = product_models.Brand.objects.all().count()
    orders = order_models.Order.objects.all().count()
    
    
    receved_orders = order_models.Order.objects.filter(status='receved').count()
    processed_orders = order_models.Order.objects.filter(status='processed').count()
    shiped_orders = order_models.Order.objects.filter(status='shiped').count()
    delivered_orders = order_models.Order.objects.filter(status='delivered').count()
  
    return render(request, 'account/dashboard.html', {
        'user':users,
        'products':products,
        'reviews':reviews,
        'categories':categories,
        'brands':brands,
        'orders':orders,
        'receved_orders':receved_orders,
        'processed_orders':processed_orders,
        'shiped_orders':shiped_orders,
        'delivered_orders':delivered_orders,
    })
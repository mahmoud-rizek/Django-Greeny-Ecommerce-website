from django.shortcuts import render, get_object_or_404
from products.models import Product
from account.models import UserAddrees, userPhoneNumber
from .models import Cart, CartDetail, Order, OrderDetail, Coupon
from django.utils.timezone import datetime
# Create your views here.



def add_to_cart(request):
    if request.method == "POST" :
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        
        product1 = Product.objects.get(id=product_id)
        card = Cart.objects.get(user=request.user, status='inprogress')
        cart_detail, created = CartDetail.objects.get_or_create(
            cart=card,
            product=product1
        )
        cart_detail.quantity = int(quantity)
        cart_detail.price = product1.price
        cart_detail.total = int(quantity) * product1.price
        cart_detail.save()
        

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    user_address = UserAddrees.objects.filter(user=request.user)
    return render(request, "orders/orders.html", {'orders':orders, 'addrees':user_address})
        

from django.http import JsonResponse
from django.template.loader import render_to_string
def checkout(request):
    cart = Cart.objects.get(user=request.user, status='inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    user_phones = userPhoneNumber.objects.filter(user=request.user)
    user_address = UserAddrees.objects.filter(user=request.user)
    date_today = datetime.today().date()
    delivery = 50

    if request.method == "POST":
        code = request.POST=['coupon_code']
        coupon_code = get_object_or_404(Coupon, code=code)
        if coupon_code and coupon_code.quantity > 0 and date_today >= coupon_code.from_date and date_today <= coupon_code.to_date:
            code_value = cart.get_total() / 100 * coupon_code.value
            total = cart.get_total() - code_value
            html = render_to_string('include/summery.html', {'reviews':all_reviews, request:request})
            return JsonResponse({'result':html})



    return render(request, "orders/checkout.html", 
                  {'cart':cart, 
                   'cart_detail':cart_detail,
                   'phones':user_phones,
                   'address':user_address,
                   })



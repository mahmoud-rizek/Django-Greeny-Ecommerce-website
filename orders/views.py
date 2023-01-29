from django.shortcuts import render
from products.models import Product
from account.models import UserAddrees
from .models import Cart, CartDetail, Order, OrderDetail
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
        

def checkout(request):
    cart = Cart.objects.get(user=request.user, status='inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)

    if request.method == "POST":
        print(request.POST)
    return render(request, "orders/checkout.html", {'cart':cart, 'cart_detail':cart_detail})


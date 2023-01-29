from .models import Cart, CartDetail


def get_or_create_card(request):
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user, status='inprogress')
        cart_detail_data = CartDetail.objects.filter(cart=cart)
        return {'cart':cart, 'cart_detail_data':cart_detail_data}
    else:
        return {}
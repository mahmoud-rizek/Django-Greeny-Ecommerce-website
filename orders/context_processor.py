from .models import Cart, CartDetail


def get_or_create_card(request):
    if request.user.is_authenticated:
        # get or create cart for user
        # created is boolen variable = True if cart is created , false if cart is already exist
        cart,created = Cart.objects.get_or_create(user=request.user, status='inprogress')
        # get cart detail for cart
        cart_detail_data = CartDetail.objects.filter(cart=cart)
        return {'cart':cart, 'cart_detail_data':cart_detail_data}
    else:
        cart = {}
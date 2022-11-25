from .models import Cart, CartDetail


def get_or_create_card(request):
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user, status='inprogress')
        return {'cart':cart}
    else:
        return {}
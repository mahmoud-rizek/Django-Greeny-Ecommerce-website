from .models import Card, CardDetail


def get_or_create_card(request):
    if request.user.is_authenticated:
        cart,created = Card.objects.get_or_create(user=request.user, status='inprogress')
        return {'cart':cart}
    else:
        return {}
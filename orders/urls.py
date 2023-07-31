from django.urls import path
from .views import add_to_cart, order_list, checkout
from .apis import OrderListAPI

app_name = 'orders'


urlpatterns = [
    path("add_to_cart", add_to_cart, name="add_to_cart"),
    path("", order_list, name="order_list"),
    path("checkout", checkout, name="checkout"),



    # APIs

    path("api/<str:username>/orders", OrderListAPI.as_view()),
]

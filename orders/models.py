from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from utils.genrate_code import genrate_code
from products.models import Product
from django.utils import timezone
# Create your models here.

STATUS_CHOICES = (
    ('receved', 'received'),
    ('processed', 'prosessed'),
    ('shiped', 'shiped'),
    ('delivered', 'delivered')
)
STATUS = (
    ('inprogress', 'inprogress'),
    ('completed', 'completed')
)


class Cart(models.Model):
    cart = models.CharField(max_length=8, default=genrate_code)
    user = models.ForeignKey(User, related_name='user_cards',
                             on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)

    def __str__(self):
        return self.cart
    
    def get_total(self):
        total = 0
        for cart_detail in self.card_detail.all():
            total += cart_detail.total
        return total


class CartDetail(models.Model):
    cart = models.ForeignKey(
        Cart, related_name='card_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='card_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    total = models.FloatField(default=True)

    def __str__(self):
        return str(self.cart)


class Order(models.Model):
    code = models.CharField(max_length=8, default=genrate_code)
    user = models.ForeignKey(User, related_name='user_orders',
                             on_delete=models.SET_NULL, null=True, blank=True)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)

    def __str__(self):
        return self.code


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='order_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantaty = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.order)



class Coupon(models.Model):
    code = models.CharField(_("Coupon"), max_length=50)
    quantity = models.IntegerField(_("Quanhtity"))
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    value = models.FloatField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
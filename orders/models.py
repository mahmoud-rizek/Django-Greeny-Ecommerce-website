from django.db import models
from django.contrib.auth.models import User
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


class Card(models.Model):
    card = models.CharField(max_length=8, default=genrate_code)
    user = models.ForeignKey(User, related_name='user_cards',
                             on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)

    def __str__(self):
        return self.card


class CardDetail(models.Model):
    card = models.ForeignKey(
        Card, related_name='card_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='card_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantaty = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.card)


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
    quantaty = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order)

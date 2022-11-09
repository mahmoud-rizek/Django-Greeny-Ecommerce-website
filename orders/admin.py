from django.contrib import admin
from .models import Card, CardDetail, Order, OrderDetail,Coupon
# Register your models here.


admin.site.register(Coupon)
admin.site.register(Card)
admin.site.register(CardDetail)
admin.site.register(Order)
admin.site.register(OrderDetail)

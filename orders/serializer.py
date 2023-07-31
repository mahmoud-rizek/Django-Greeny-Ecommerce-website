from rest_framework import serializers

from .models import Order, OrderDetail

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        quary_set = Order()
        fields = '__all__'
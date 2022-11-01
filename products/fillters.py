from django_filters import rest_framework
from .models import product


class productFillter(rest_framework.FilterSet):
    class Meta:
        model = product
        fields = {
            'name' : ['icontains'],
            'price' : ['lte', 'gte'],
        }
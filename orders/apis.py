from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from .serializers import oerderSerializer
from .models import Order, OrderDetail
from django.contrib.auth.models import User





class OrderListAPI(generics.ListCreateAPIView):

    queryset = Order.objects.all()
    # serializer_class = OrderSerializer


    def list (self, request, *args, **kwargs):
        user = User.objects.get( username=self.kwargs['username'])
        queryset = Order.objects.all().filter(user=user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)





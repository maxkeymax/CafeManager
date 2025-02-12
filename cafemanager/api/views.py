from rest_framework import generics
from order.models import Order
from .serializers import OrderSerializer

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
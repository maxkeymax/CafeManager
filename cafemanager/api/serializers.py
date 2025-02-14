import json
from order.models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('id', 'table_number', 'items', 'total_price')

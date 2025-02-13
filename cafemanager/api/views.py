import json
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from order.models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        items_str = serializer.validated_data.get('items')
        
        try:
            items = Order.parse_items(items_str)
        except ValueError as e:
            raise ValidationError({'items': str(e)})
            
        total_price = sum(item['price'] for item in items)
        items_to_json = json.dumps(items)
        status = 'В ожидании'
        
        serializer.save(total_price=total_price, status=status, items=items_to_json)
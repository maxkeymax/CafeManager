import json
from order.models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'items' in ret:
            ret['items'] = json.loads(ret['items'])
        return ret
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('id', 'table_number', 'items')
        labels = {
            'id': 'Заказ №',
            'table_number': 'Стол №',
            'items': 'Блюдо/Стоимость (через запятую)',
        }
        widgets = {
            'items': forms.Textarea(attrs={'rows': 5}),
        }
       
    def save(self, commit=True):
        instance = super().save(commit=False)
        items = instance.items
        if items:
            total_price = 0
            for item in items.split(','):
                try:
                    _, price = item.split('/')
                    total_price += int(price)
                except ValueError:
                    raise forms.ValidationError('Неправильный формат ввода блюд и цен')
            instance.total_price = total_price
        if commit:
            instance.save()
        return instance
    
    
class OrderFilterForm(forms.Form):
    order_id = forms.IntegerField(label='Заказ №', required=False) 
    table_number = forms.IntegerField(label='Стол №', required=False)
    status = forms.ChoiceField(label='Статус', choices=[('Все', 'Все')] + Order.STATUS_CHOISES, required=False)
    
    
class OrderStatusForm(forms.Form):
    status = forms.ChoiceField(label='Статус', choices=Order.STATUS_CHOISES, required=True)
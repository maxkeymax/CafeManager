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
       
    def clean_items(self):
        items = self.cleaned_data['items']
        total_price = 0
        for item in items.split(','):
            if '/' in item:
                try:
                    _, price = item.split('/')
                    total_price += int(price)
                except ValueError:
                    raise forms.ValidationError('Неправильный формат ввода блюд и цен')
            else:
                raise forms.ValidationError('Неправильный формат ввода блюд и цен')
        self.cleaned_data['total_price'] = total_price
        return items
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total_price = self.cleaned_data['total_price']
        if commit:
            instance.save()
        return instance
    
    
class OrderFilterForm(forms.Form):
    order_id = forms.IntegerField(label='Заказ №', required=False) 
    table_number = forms.IntegerField(label='Стол №', required=False)
    status = forms.ChoiceField(label='Статус', choices=[('Все', 'Все')] + Order.STATUS_CHOISES, required=False)
    
    
class OrderStatusForm(forms.Form):
    status = forms.ChoiceField(label='Статус', choices=Order.STATUS_CHOISES, required=True)
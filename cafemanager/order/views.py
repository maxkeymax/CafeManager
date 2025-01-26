from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import OrderForm, OrderFilterForm
from .models import Order

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_order')
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})


class OrderListView(ListView):
    model = Order
    template_name = 'order/orders_management.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderFilterForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = OrderFilterForm(self.request.GET)
        if form.is_valid():
            table_number = form.cleaned_data['table_number']
            status = form.cleaned_data['status']
            if table_number:
                queryset = queryset.filter(table_number=table_number)
            if status and status != 'все':
                queryset = queryset.filter(status=status)
        return queryset

def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('orders_management')
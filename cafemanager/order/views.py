from django.shortcuts import render, redirect
from .forms import OrderForm

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_order')
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})
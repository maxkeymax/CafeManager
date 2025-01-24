from django.shortcuts import render

def add_order(request):
    return render(request, 'order/add_order.html')

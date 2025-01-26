from django.urls import path

from . import views

urlpatterns = [
    path('add_order/', views.add_order, name='add_order'),
    path('orders-management/', views.OrderListView.as_view(), name='orders_management'),
    path('delete/<pk>/', views.delete_order, name='delete_order'),
]

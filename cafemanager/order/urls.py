from django.urls import path

from . import views

urlpatterns = [
    path('add_order/', views.add_order.as_view(), name='add_order'),
    path('delete_order/', views.delete_order.as_view(), name='delete_order'),
    path('search_order/', views.search_order.as_view(), name='search_order'),
    path('order_list', views.order_list.as_view(), name='order_list'),
    path('change_status', views.change_status.as_view(), name='change_status'),
    
]

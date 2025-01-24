from django.urls import path

from . import views

urlpatterns = [
    path('add_order/', views.add_order, name='add_order'),
    # path('delete_order/', views.delete_order, name='delete_order'),
    # path('search_order/', views.search_order, name='search_order'),
    # path('order_list/', views.order_list, name='order_list'),
    # path('change_status/', views.change_status, name='change_status'),
    
]

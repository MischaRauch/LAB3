from os import name
from django.urls import path

from . import views

urlpatterns = [
    #get
    path('test', views.test),
    path('', views.get_all_pizzas, name='index'),
    path('<int:pizza_id>/', views.get_one_pizza, name='detail'),
    path('veggi/<int:pizza_id>/', views.get_vegetarian),
    path('drinks', views.get_drinks),
    path('drinks/<int:drink_id>/', views.get_drink_price),
    path('deserts', views.get_deserts),                             #method doesnt exist? 
    path('desert/<int:desert_id>/', views.get_desert_price),
    path('orders', views.get_orders),
    path('showorder', views.get_show_order),  
    
    #post
    path('login', views.get_customer),
    path('createCustomer', views.create_customer),
    path('createOrderItem', views.create_order_item),
    path('orders/<int:order_id>/', views.update_order_status)
    
#    path('query', views.query)
]
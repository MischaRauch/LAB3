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
    path('deserts', views.get_deserts),                             
    path('desert/<int:desert_id>/', views.get_desert_price),
    path('orders', views.get_orders),
    path('showorder', views.get_show_order),  
    path('deliveryestimation', views.get_delivery_estimation),
    #path('getDeliveryTimeAndStatus/<int:order_id>/', views.get_delivery_time_and_status_from_order),   #TODO continue , sorry mimi dont hate me <3 
    
    #TRIGGER 


    #post
    path('login', views.get_customer),
    path('createCustomer', views.create_customer),
    path('createOrderItem', views.create_order_item),
    path('orders/<int:order_id>/', views.update_order_status),
    path('updateEmployees', views.update_employee_status),
    path('cancelOrder', views.cancel_order),
    path('orderinfo', views.order_info)

#    path('query', views.query)
]
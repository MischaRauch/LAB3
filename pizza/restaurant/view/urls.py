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
    
    #post
    path('login', views.get_customer),
    path('createCustomer', views.create_customer),
    path('createOrderItem', views.create_order_item),
    
#    path('query', views.query)
]
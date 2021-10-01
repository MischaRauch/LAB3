from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pizza_id>/', views.detail, name='detail'),
    path('listpizza', views.listpizzas, name='gallery'),
    path('createCustomer', views.create_Customer),
    
#    path('query', views.query)
]
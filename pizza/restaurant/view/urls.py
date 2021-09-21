from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pizza_id>/', views.detail, name='detail'),
    path('listpizza', views.listpizzas, name='gallery'),
    path('query', views.query)
]
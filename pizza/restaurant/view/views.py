from django.shortcuts import get_object_or_404, render

from restaurant.model.models import pizza
from django.db import connection


def index(request):
    pizza_list = pizza.objects.order_by('-pizza_id')[:5]
    context = {'pizza_list': pizza_list}
    return render(request, 'restaurant/index.html', context)

def detail(request, pizza_id):
    selected_pizza = get_object_or_404(pizza, pk=pizza_id)
    #pizza = get_object_or_404(pizza_id, pk)
    return render(request, 'restaurant/detail.html', {'pizza': selected_pizza})

def listpizzas(request):
    return render(request, 'restaurant/gallery.html')

def my_custom_sql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu_pizza")
    row = cursor.fetchall()
    return row

def query(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu_pizza WHERE pizza_id = 1")
    row = cursor.fetchall()
    print(row)
    return render(row,'detail.html')

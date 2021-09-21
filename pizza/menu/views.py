from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import pizza


def index(request):
    pizza_list = pizza.objects.order_by('-pizza_id')[:5]
    context = {'pizza_list': pizza_list}
    return render(request, 'menu/index.html', context)

def detail(request, pizza_id):
    selected_pizza = get_object_or_404(pizza, pk=pizza_id)
    #pizza = get_object_or_404(pizza_id, pk)
    return render(request, 'menu/detail.html', {'pizza': selected_pizza})

def listpizzas(request):
    return render(request, 'menu/gallery.html')

def my_custom_sql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu_pizza")
    row = cursor.fetchall()
    return row

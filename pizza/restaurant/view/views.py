from django.shortcuts import get_object_or_404, render

from restaurant.model.models import pizza


def index(request):
    pizza_list = pizza.objects.order_by('-pizza_id')
    context = {'pizza_list': pizza_list}
    return render(request, 'restaurant/index.html', context)
    

def detail(request, pizza_id):
    selected_pizza = get_object_or_404(pizza, pk=pizza_id)
    sel = pizza.objects.get(pk=pizza_id)
    #seol = pizza.objects.filter(pizza_id= 2)
    print(sel)
    #pizza = get_object_or_404(pizza_id, pk)
    get_pizza_toppings(request)
    return render(request, 'restaurant/selectPizzaToppings.html', {'pizza': selected_pizza})

def listpizzas(request):
    return render(request, 'restaurant/gallery.html')

def get_pizza_toppings(request):
    print("GOt HErE")
    #return render(request, 'restaurant/selectPizzaToppings.html')
    

#def my_custom_sql():
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM menu_pizza")
#    row = cursor.fetchall()
#    return row
#
#def query(request):
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM menu_pizza WHERE pizza_id = 1")
#    row = cursor.fetchall()
#    print(row)
#    return render(row,'detail.html')

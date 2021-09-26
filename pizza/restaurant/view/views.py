
from django.shortcuts import get_object_or_404, render
from restaurant.controller import queries 
from restaurant.model.models import pizza

def index(request):
    pizza_list = pizza.objects.order_by('-pizza_id')
    context = {'pizza_list': pizza_list}
    return render(request, 'restaurant/index.html', context)
    

def detail(request, pizza_id): 
    selected_pizza = get_object_or_404(pizza, pk=pizza_id)
    print ('im here          ' )
    #test 
    check_price = queries.get_pizza_price(1)
    print (' PRICE PIZZA   ' , check_price)
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

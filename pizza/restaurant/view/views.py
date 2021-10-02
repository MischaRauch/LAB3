
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
   #check_address = queries.create_address_customer(postal_code= '61rpp', country= 'nl', street= 'capu', house_number= 11, city= 'maas', first_name='ollie', last_name= 'rock', email='whatever ', phone= 69)  
   # new_order = queries.create_new_order_old_customer('1') 
    #print (' check address  ' , new_order)
    queries.update_price_of_order(4)
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

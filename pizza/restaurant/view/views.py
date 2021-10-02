from datetime import date
import json
import re
from sys import set_asyncgen_hooks
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from restaurant.controller import queries 
from restaurant.model.models import pizza, drink, desert
from django.core import serializers


#For testing purposes
def test(request):
    print ('im here          ' )
   # check_price = queries.get_pizza_price(1)
   # print (' PRICE PIZZA   ' , check_price)
   # check_address = queries.create_address_customer(postal_code= '61rpp', country= 'nl', street= 'capu', house_number= 11, city= 'maas', first_name='ollie', last_name= 'rock', email='whatever ', phone= 69)  
   # new_order = queries.create_new_order_old_customer('1') 
   # print (' check address  ' , new_order)
   # queries.create_order_item(new_order, quantity= 2, pizza_id= 1)
    return HttpResponse('Success')

#returns all pizzas
def get_all_pizzas(request):
    pizza_list = pizza.objects.order_by('-pizza_id')
    print("RAW DATA: ", pizza_list)
    #print(model_to_dict(pizza_list))
    data = serializers.serialize('json', pizza_list, fields=('pizza_id','pizza_name'))
    return JsonResponse(data, safe= False)
    
#returns one pizza with ingridients and price
def get_one_pizza(request, pizza_id): 
    toppings = queries.get_toppings(pizza_id)
    price = queries.get_pizza_price(pizza_id)
    toppings.append(price)    
    toppings = json.dumps(toppings)
    return JsonResponse(str(toppings), safe= False)

#returns true or false if pizza is vegeterian
def get_vegetarian(request, pizza_id):
    veggi = queries.is_pizza_vegetarian(pizza_id)
    print('VEGGI ',veggi)
    data = json.dumps(veggi)
    return JsonResponse(data, safe=False)

def get_drinks(request):
    drink_list = drink.objects.order_by('-drink_id')
    data = serializers.serialize('json', drink_list, fields=('drink_id','drink_name'))
    return JsonResponse(data, safe= False)

def get_drink_price(request, drink_id):
    price = queries.get_drink_price(drink_id)
    data = json.dumps(price)
    return JsonResponse(data, safe=False)

def get_deserts(request):
    drink_list = desert.objects.order_by('-desert_id')
    data = serializers.serialize('json', drink_list, fields=('desert_id','desert_name'))
    return JsonResponse(data, safe= False)

def get_desert_price(request, desert_id):
    price = queries.get_desert_price(desert_id)
    data = json.dumps(price)
    return JsonResponse(data, safe=False)


#creates a customer
@csrf_exempt
def create_customer(request):
    if (request.method == 'POST'):
        print("DATA" ,request.POST['first_name'])
        #postal_code, country, street, house_number, city, first_name, last_name, email, phone
        global new_order
        new_order = queries.create_new_order_new_customer(request.POST['postal_code'],request.POST['country'],request.POST['street'],request.POST['house_number'],request.POST['city'],request.POST['first_name'], request.POST['last_name'],request.POST['email'],request.POST['phone'])
        print("NEW ORDER ",new_order)
    else:
        print('NO POST')
   # request.session['order'] = new_order
   # if new_order is None:
   #     order = new_order
   # print("ORDER ", request.sesssion.get('order'))
    
    #queries.create_address_customer(request)
    return HttpResponse('Success')

@csrf_exempt
def get_customer(request):
    if (request.method == 'POST'):
        global new_order
        new_order = queries.create_new_order_old_customer(request.POST['customer_id'])
    else:
        print('NO POST')
    return HttpResponse('Success')

@csrf_exempt
def create_order_item(request):
    print('CUSTOMER ', new_order)
    if (request.method == 'POST'):     
        print('GOT HERE')
        print(type(request.POST['drink_id']))
        print(request.POST['desert_id'])
        print(((request.POST['drink_id']) == '9999') and ((request.POST['desert_id']) == '9999'))
        if (((request.POST['drink_id']) == '9999') and ((request.POST['desert_id']) == '9999') ):
            print('Pizza_id', request.POST['pizza_id'])
            queries.create_order_item(new_order, request.POST['quantity'], request.POST['pizza_id'])
        if (((request.POST['pizza_id']) == '9999') and ((request.POST['desert_id']) == '9999') ):
            print('Drink_ID')
            queries.create_order_item(new_order, request.POST['quantity'], None, request.POST['drink_id'])
        if (((request.POST['pizza_id']) == '9999') and ((request.POST['drink_id']) == '9999') ):
            print('Dessert_Id')
            queries.create_order_item(new_order, request.POST['quantity'], None, None,  request.POST['desert_id'])
        
    else:
        print('NO POST')
    
    return HttpResponse('Success')














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

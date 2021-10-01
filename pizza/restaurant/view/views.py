
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from restaurant.controller import queries 
from restaurant.model.models import pizza
from django.core import serializers

def index(request):
    pizza_list = pizza.objects.order_by('-pizza_id')
    print("RAW DATA: ", pizza_list)
    #context = {'pizza_list': pizza_list}
    data = serializers.serialize('json', pizza_list, fields=('pizza_id','pizza_name'))
    return JsonResponse(data, safe= False)
    #return render(request, 'restaurant/index.html', context)
    

def detail(request, pizza_id): 
    selected_pizza = get_object_or_404(pizza, pk=pizza_id)
    print ('im here          ' )
    #test 
    #check_price = queries.get_pizza_price(1)
    queries.get_pizza_name(pizza_id)
    #print (' PRICE PIZZA   ' , check_price)
    return render(request, 'restaurant/selectPizzaToppings.html', {'pizza': selected_pizza})

@csrf_exempt
def create_Customer(request):
    if (request.method == 'POST'):
        print("DATA" ,request.POST['first_name'])
        #postal_code, country, street, house_number, city, first_name, last_name, email, phone
        queries.create_address_customer(request.POST['postal_code'],request.POST['country'],request.POST['street'],request.POST['house_number'],request.POST['city'],request.POST['first_name'], request.POST['last_name'],request.POST['email'],request.POST['phone'])
    else:
        print('NO POST')
    #queries.create_address_customer(request)
    return HttpResponse('Success')


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

#return one pizza
from restaurant.model.models import pizza_toppings
from restaurant.model.models import topping
from restaurant.model.models import pizza,desert,drink, address, customer   
from django.db import models


#returns 1 pizza id based on id
def get_pizzas(id): 
	return pizza.objects.get(pizza_id= id)  

#return 1 pizza name 
def get_pizza_name(id):
	print("TEST ",pizza.objects.only('pizza_name').get(pk=id))
	return pizza.objects.only('pizza_name').get(pk=id)

def get_desert(id): 
	return desert.objects.get(desert_id= id) 

def get_desert_name(id):
	return desert.objects.only('desert_name').get(pk=id)

def get_drink(id): 
	return drink.objects.get(drink_id= id) 

def get_drink_name(id):
	return drink.objects.only('drink_name').get(pk=id)


#returns desert price 
def get_desert_price(id):
	test = desert.objects.filter(desert_id = id).values('desert_price')
	for selected_desert in test:
		return selected_desert.get('desert_price')

#returns drink price 
def get_drink_price(id):
	test = drink.objects.filter(drink_id = id).values('drink_price')
	for selected_drink in test:
		return selected_drink.get('drink_price')

#returns topping price 
def get_topping_price(id):
	test = topping.objects.filter(topping_id = id).values('topping_price')
	for selected_toping in test:
		return selected_toping.get('topping_price')

#returns price of entire pizza 
def get_pizza_price(id): 
	list_of_toppings = pizza_toppings.objects.filter(pizza_id=id).values('pizza_toppings_id', 'pizza_id', 'topping_id') #getting all pizza_toppings for 1 pizza 
	price = 0
	for p_topping in list_of_toppings:
		price += get_topping_price(p_topping.get('topping_id'))
	return price 


#returns true or false if toopping is vegetarian 
def is_topping_vegetarian(id):
	test = topping.objects.filter(topping_id = id).values('vegeterian')
	for selected_topping in test:
		if selected_topping.get('vegeterian') == True:
			return True
	return False

#return if pizza is veg 
def is_pizza_vegetarian(id):	
	list_of_toppings = pizza_toppings.objects.filter(pizza_id=id).values('pizza_toppings_id', 'pizza_id', 'topping_id')
	for p_topping in list_of_toppings:
		if (not is_topping_vegetarian( p_topping.get('topping_id') )):  
			return False 
	return True 

	
def create_address_customer(postal_code, country, street, house_number, city, first_name, last_name, email, phone):
    #first create address
    new_address_id = create_only_address(postal_code= postal_code, country= country, street= street, house_number= house_number, city= city)
    #after address creation we can create a customer
    create_only_customer(first_name= first_name, last_name= last_name, email= email, phone= phone, address_id= new_address_id)


def create_only_address(postal_code, country, street, house_number, city):
    #create new address
    new_adress = address.objects.get_or_create(postal_code= postal_code, country= country, street= street, house_number= house_number, city= city)
    #tuple needs name to get address and flag if object created or not
    (customer_address, flag) = new_adress
    return customer_address

def create_only_customer(first_name, last_name, email, phone, address_id):
    #create new customer based on address information
    customer.objects.get_or_create(first_name= first_name, last_name= last_name, email_address= email, phone_number= phone, address_id = address_id)
#return one pizza
from django.db.models.lookups import PostgresOperatorLookup
from restaurant.model.models import pizza_toppings
from restaurant.model.models import topping
from restaurant.model.models import pizza,desert,drink, address, customer, order_item, employee , orders, order_item, delivery 
from django.utils.timezone import now 
from datetime import datetime 


#returns 1 pizza id based on id
def get_pizza_by_id(id): 
	return pizza.objects.filter(pizza_id= id)[0]  

#return 1 pizza name 
def get_pizza_name(id):
	return pizza.objects.only('pizza_name').get(pk=id)

def get_desert_by_id(id): 
	return desert.objects.filter(desert_id= id)[0]   

def get_desert_name(id):
	return desert.objects.only('desert_name').get(pk=id)

def get_drink_by_id(id): 
	return drink.objects.filter(drink_id= id)[0]  

def get_drink_name(id):
	return drink.objects.only('drink_name').get(pk=id)

def get_customer_by_id(id):
	return customer.objects.filter(customer_id = id)[0]
	



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


def get_employee_based_on_user_postal_code(postal_code): 
	#return employee object based on postal code 
	employ = employee.objects.filter(area_code = postal_code[:2]) #gettin emplyee with area code == to the first 2 digits from postal code. 0 because is an array 
	return employ[0] 



def get_delivery_id(delivery_object):
	test = delivery.objects.filter().values('delivery_id')
	for selected_delivery in test:
		return selected_delivery.get('delivery_id')


#MAYBE NOT NEEDED return area code from employee 
def get_area_code(employee_id):
	test = employee.objects.filter(employee_id = id).values('area_code')
	for selected_employee in test:
		return selected_employee.get('area_code')



def is_topping_vegetarian(id):
	#returns true or false if toopping is vegetarian 
	test = topping.objects.filter(topping_id = id).values('vegeterian')
	for selected_topping in test:
		if selected_topping.get('vegeterian') == True:
			return True
	return False


def is_pizza_vegetarian(id):
	#return if pizza is veg 	
	list_of_toppings = pizza_toppings.objects.filter(pizza_id=id).values('pizza_toppings_id', 'pizza_id', 'topping_id')
	for p_topping in list_of_toppings:
		if (not is_topping_vegetarian( p_topping.get('topping_id') )):  
			return False 
	return True 
	

def create_address_customer(postal_code, country, street, house_number, city, first_name, last_name, email, phone):
    #first create address
    new_address = create_only_address(postal_code= postal_code, country= country, street= street, house_number= house_number, city= city)
    #after address creation we can create a customer
    new_customer = create_only_customer(first_name= first_name, last_name= last_name, email= email, phone= phone, address_id= new_address)
    return new_customer
	

def create_new_order_new_customer(postal_code, country, street, house_number, city, first_name, last_name, email, phone):
	#create an address and customer 
	# TODO
	new_customer = create_address_customer(postal_code= postal_code, country= country, street= street, house_number= house_number, city= city, first_name= first_name, last_name= last_name, email=email, phone= phone)
	
	#FIND OUT CUSTOMER_ID to pass to new method
	print(new_customer.customer_id)
	create_new_order_old_customer(new_customer.customer_id)

def create_new_order_old_customer(customer_id):
	#get customer postal code 
	customer_postal_code= get_postal_code(customer_id)
	print ('line 107' , customer_postal_code)
	#find out employee 
	employee_object = get_employee_based_on_user_postal_code(customer_postal_code)
	print ('line 110' , employee_object)
	#create delivery first 
	new_delivery = create_delivery(employee_object)
	
	total_price= 0 #need to update it after 
	total_discount = 0 #need to update it after
	new_order = orders.objects.create(customer_id = get_customer_by_id(customer_id), total_price= total_price, total_discount = total_discount, delivery_id = new_delivery  )
	return new_order 


def create_order_item(order_object, quantity,  pizza_id= None, drink_id= None, desert_id=None ): 
	if pizza_id:
		#get pizza object  
		print('line 135')
		pizza_object = get_pizza_by_id(pizza_id)
		print('pizza_object    ', pizza_object)

		order_item.objects.create(pizza_id = pizza_object, quantity= quantity, order_id = order_object)
	elif drink_id:
		#get drink object 
		drink_object = get_drink_by_id(drink_id)
		order_item.objects.create(drink_id = drink_object, quantity= quantity, order_id = order_object)
	elif desert_id: 
		#get desert object 
		desert_object = get_desert_by_id(desert_id)
		order_item.objects.create(desert_id = desert_object, quantity= quantity, order_id = order_object)

def create_delivery (employee_object): 
	new_delivery = delivery.objects.create(employee_id= employee_object, status= 'Preparation')
	return new_delivery

def update_delivery_status(delivery_id, new_status):
	"""
	Updates delivery to new status.

	Returns number of rows changed. Will be 0 if id is not matched
	"""
	number_or_rows_changed = delivery.objects.filter(delivery_id=delivery_id).update(status=new_status)
	
	return number_or_rows_changed

def create_new_order_item(pizza_id, drink_id, desert_id, quantity, order_id):
	new_order_item = order_item.obejcts.create(quantity = quantity, pizza_id= pizza_id, drink_id= drink_id, desert_id = desert_id, irder_id=order_id )
	return new_order_item 


def create_only_address(postal_code, country, street, house_number, city):
    #create new address
    new_adress = address.objects.get_or_create(postal_code= postal_code, country= country, street= street, house_number= house_number, city= city)
    #tuple needs name to get address and flag if object created or not
    (customer_address, flag) = new_adress
    return customer_address

def create_only_customer(first_name, last_name, email, phone, address_id):
    #create new customer based on address information
	new_customer = customer.objects.get_or_create(first_name= first_name, last_name= last_name, email_address= email, phone_number= phone, address_id = address_id)
	return new_customer[0]

def update_price_of_order(order_id):
	"""
	Get all order items. Get price of all items
	Update Order.Total_price

	Returns price of order
	"""
	vat = 0.09
	margin_of_profit = 0.4
	total_order_price = 0
	all_pizza_items =order_item.objects.filter(order_id=order_id, pizza_id__isnull=False).values('pizza_id')
	all_drink_items =order_item.objects.filter(order_id=order_id, drink_id__isnull=False).values('drink_id')
	all_desert_items =order_item.objects.filter(order_id=order_id, desert_id__isnull=False).values('desert_id')

	for pizza_item in all_pizza_items:
		pizza = get_pizza_by_id(pizza_item.get('pizza_id'))
		total_order_price += get_pizza_price(pizza)
	
	for drink_item in all_drink_items:
		drink = get_drink_by_id(drink_item.get('drink_id'))
		total_order_price += get_drink_price(drink)

	for desert_item in all_desert_items:
		desert = get_desert_by_id(desert_item.get('desert_id'))
		total_order_price +=get_desert_price(desert)

	total_order_price += (total_order_price * vat) + ( total_order_price * margin_of_profit)

	orders.objects.filter(order_id=order_id).update(total_price=total_order_price)

	return total_order_price



#returns customer postal code 
def get_postal_code(id):
	test = customer.objects.filter(customer_id = id).values('address_id')
	for selected_customer in test:
		address_idd= selected_customer.get('address_id')	
	test = address.objects.filter(address_id = address_idd).values('postal_code')
	for selected_customer in test:
		print( selected_customer.get('postal_code'))
		return selected_customer.get('postal_code')
	

"""

Change delivery status after 5 mins, delivered after 15


Method delete order (only possible in first 5 mins)
"""
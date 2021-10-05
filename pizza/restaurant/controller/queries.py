#return one pizza
from os import name

from django.db import models
from restaurant.model.models import pizza_toppings
from restaurant.model.models import topping
from restaurant.model.models import pizza,desert,drink, address, customer, order_item, employee , orders, order_item, delivery 
from django.utils.timezone import now 
from datetime import datetime 
from django.db.models import F
from datetime import datetime, timedelta 

#TODO change or delete the pk methods
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
	

#returns desert price including VAT and marging of profit   
def get_desert_price(id):
	vat = 0.09
	margin_of_profit = 0.4
	price = 0
	test = desert.objects.filter(desert_name = id).values('desert_price')
	for selected_desert in test:
		price = selected_desert.get('desert_price')
	return price + price*vat + price*margin_of_profit

#returns drink price including VAT and marging of profit   
def get_drink_price(id):
	print("WHATS THAT ", id)
	vat = 0.09
	margin_of_profit = 0.4
	price = 0
	test = drink.objects.filter(drink_name = id).values('drink_price')
	for selected_drink in test:
		price = selected_drink.get('drink_price')
	return price + price*vat + price*margin_of_profit

#returns topping price including VAT and marging of profit   
def get_topping_price(id):

	vat = 0.09
	margin_of_profit = 0.4
	price = 0
	test = topping.objects.filter(topping_id = id).values('topping_price')
	for selected_toping in test:
		price=  selected_toping.get('topping_price')		
	return price + price*vat + price*margin_of_profit

#returns price of entire pizza 
def get_pizza_price(id): 
	list_of_toppings = pizza_toppings.objects.filter(pizza_id=id).values('pizza_toppings_id', 'pizza_id', 'topping_id') #getting all pizza_toppings for 1 pizza 
	price = 0
	for p_topping in list_of_toppings:
		price += get_topping_price(p_topping.get('topping_id'))
	return price 

#returns list of toppings of a pizza
def get_toppings(id):
	list_of_toppings = pizza_toppings.objects.filter(pizza_id=id).values('pizza_toppings_id', 'pizza_id', 'topping_id') #getting all pizza_toppings for 1 pizza 
	named_toppings = []
	for pizza in list_of_toppings:
		entry = list(topping.objects.filter(topping_id=pizza.get('topping_id')).values('topping_name'))
		print(entry)
		named_toppings.append(entry)
	return list(named_toppings)


def get_employee_based_on_user_postal_code(postal_code): 
	#return employee object based on postal code 
	employ = employee.objects.filter(area_code = postal_code[:2]) #gettin emplyee with area code == to the first 2 digits from postal code. 0 because is an array 
	return employ[0] 

#returns customer postal code 
def get_postal_code(id):
	test = customer.objects.filter(customer_id = id).values('address_id')
	for selected_customer in test:
		address_idd= selected_customer.get('address_id')	
	test = address.objects.filter(address_id = address_idd).values('postal_code')
	for selected_customer in test:
		print( selected_customer.get('postal_code'))
		return selected_customer.get('postal_code')
	
def get_delivery_id(delivery_object):
	test = delivery.objects.filter().values('delivery_id')
	for selected_delivery in test:
		return selected_delivery.get('delivery_id')

#TODO connect it to app_manager ALSO add button in GUI that gives this option  
def get_delivery_time_and_status_from_order(order_id):
	order_info = orders.objects.filter(order_id=order_id).values('order_time', 'delivery_id')[0]
	delivery_info = delivery.objects.filter(delivery_id = order_info['delivery_id']).values('status')[0]
	time_change = timedelta(minutes=15)
	new_time = order_info['order_time'] + time_change 
	information = 'Status of order:', delivery_info['status'] , order_info['order_time'].strftime('. The order was made at %H:%M'),  new_time.strftime('. Arrival time: %H:%M') 
	print (information)
	return information 



def update_employee_status():
	employees_delivering = employee.objects.filter(status_employee ='On delivery').values('employee_id')
	current_time = datetime.now()
	for emp in employees_delivering:
		print("EMPP ", delivery.objects.filter(employee_id = emp['employee_id'], status = 'Received by customer').values['delivery_id'])
		deliveries = delivery.objects.filter(employee_id = emp['employee_id'], status = 'Received by customer').values['delivery_id'] 
		should_you_update= True 
		for deliv in deliveries:
			ord = orders.objects.filter(deliery_id = deliv['delivery_id']).values['order_time'][0]
			if (current_time - ord['order_time']) > 30*60:  
				should_you_update= False
				break 
		if should_you_update:
			employee.objects.filter(employee_id=emp['employee_id']).update(status='Free')
	return employees_delivering 


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
	new_customer = create_address_customer(postal_code= postal_code, country= country, street= street, house_number= house_number, city= city, first_name= first_name, last_name= last_name, email=email, phone= phone)
	#FIND OUT CUSTOMER_ID to pass to new method
	create_new_order_old_customer(new_customer.customer_id)
	#has to return the order id not the customer
	order = orders.objects.filter(customer_id=new_customer.customer_id).first()
	return order

def create_new_order_old_customer(customer_id):
	#get customer postal code 
	customer_postal_code= get_postal_code(customer_id)
	#find out employee 
	employee_object = get_employee_based_on_user_postal_code(customer_postal_code)
	employee_delivery = employee.objects.filter(employee_id=employee_object.employee_id).values('status_employee') 
	#print("GOT HERE ",employee_object)
	#print("GOT HERE 2",employee_delivery)
	for employ in employee_delivery:
		emp = employ['status_employee']
	#	print("WORKS ", emp)
	#print("GOT HERE 3",employee_delivery['status_employee'])
	if emp == 'On delivery': 
		return False 	
	employee.objects.filter(employee_id=employee_object.employee_id).update(status_employee='On delivery')
	
	#create delivery first 
	new_delivery = create_delivery(employee_object)
	#increase discount level by 1
	customer.objects.filter(customer_id=customer_id).update(discount_available=F('discount_available') + 1)
	discount = customer.objects.filter(customer_id=customer_id).values('discount_available')
	total_price= 0 #need to update it after 
	total_discount = 0 #need to update it after
	for count in discount:
		if (count['discount_available'] >= 4):
			total_discount = 5	

	new_order = orders.objects.create(customer_id = get_customer_by_id(customer_id), total_price= total_price, total_discount = total_discount, delivery_id = new_delivery  )
	return new_order 



def create_order_item(order_object, quantity,  pizza_id= None, drink_id= None, desert_id=None ): 
	if pizza_id:
		#get pizza object  
		print('line 135')
		pizza_object = get_pizza_by_id(pizza_id)
		print('pizza_object    ', pizza_object)
		print('VALUE ', order_object)
		print('value type ',type(order_object))

		order_item.objects.create(pizza_id = pizza_object, quantity= quantity, order_id = order_object)
	elif drink_id:
		#get drink object 
		drink_object = get_drink_by_id(drink_id)
		order_item.objects.create(drink_id = drink_object, quantity= quantity, order_id = order_object)
	elif desert_id: 
		#get desert object 
		desert_object = get_desert_by_id(desert_id)
		order_item.objects.create(desert_id = desert_object, quantity= quantity, order_id = order_object)

	#calculate price and update
	order_int = getattr(order_object, 'order_id')
	update_price_of_order(order_int)

def get_orders_by_delivery_status(status):
	order_results = []
	deliveries = delivery.objects.filter(status=status)
	for deliv in deliveries:
		order = orders.objects.filter(delivery_id=deliv)[0]
		order_results.append(order)
	return order_results

def create_delivery (employee_object): 
	new_delivery = delivery.objects.create(employee_id= employee_object, status= 'Preparation')
	return new_delivery

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


def update_delivery_status_using_order_id(order_id, new_status):
	"""
	Updates delivery to new status. Using the order ID.

	Returns number of rows changed. Will be 0 if id is not matched
	"""
	delivery_obj = orders.objects.filter(order_id=order_id).values('delivery_id')[0]
	number_or_rows_changed = delivery.objects.filter(delivery_id=delivery_obj['delivery_id']).update(status=new_status)
	
	return number_or_rows_changed

#TODO add discount 
def update_price_of_order(order_id):
	"""
	Get all order items. Get price of all items
	Update Order.Total_price

	Returns price of order
	"""
	total_order_price = 0
	all_pizza_items =order_item.objects.filter(order_id=order_id, pizza_id__isnull=False).values('pizza_id')
	all_drink_items =order_item.objects.filter(order_id=order_id, drink_id__isnull=False).values('drink_id')
	all_desert_items =order_item.objects.filter(order_id=order_id, desert_id__isnull=False).values('desert_id')
	quantity = order_item.objects.filter(order_id=order_id).values('quantity')
	
	for i in quantity:
		quant = i['quantity']

	for pizza_item in all_pizza_items:
		pizza = get_pizza_by_id(pizza_item.get('pizza_id'))
		total_order_price += get_pizza_price(pizza) * quant
	
	for drink_item in all_drink_items:
		drink = get_drink_by_id(drink_item.get('drink_id'))
		total_order_price += get_drink_price(drink) * quant

	for desert_item in all_desert_items:
		desert = get_desert_by_id(desert_item.get('desert_id'))
		total_order_price +=get_desert_price(desert) * quant

	discount = orders.objects.filter(order_id=order_id).values('total_discount')
	print('PRIZE ', total_order_price)
	for disc in discount:
		if (disc['total_discount'] > 0):
			total_order_price = total_order_price - disc['total_discount']
			customer_id = orders.objects.filter(order_id=order_id).values('customer_id')
			for fo in customer_id:
				print('RESET DISCOUNT ', fo)
				customer.objects.filter(customer_id=fo['customer_id']).update(discount_available=F('discount_available') == 0)
	print('DISCOUNT ', total_order_price)
	#if(orders.objects.filter(order_id=order_id).filter('total_discount'))

	orders.objects.filter(order_id=order_id).update(total_price=total_order_price)

	return total_order_price

def update_employee_status_using_order_id(order_id, new_status): 
	delivery_obj = orders.objects.filter(order_id=order_id).values('delivery_id')[0]
	delivery_obj2= delivery.objects.filter(delivery_id=delivery_obj['delivery_id'] ).values('employee_id')[0]
	employee_object = employee.objects.filter(employee_id = delivery_obj2['employee_id']).values('employee_id')[0]
	number_or_rows_changed = employee.objects.filter(employee_id=employee_object['employee_id']).update(status=new_status)

	return number_or_rows_changed

def get_show_order(order_id):
	#get ordered items and quantity and return it as a list
	choosen_stuff = order_item.objects.filter(order_id=order_id.order_id).values('pizza_id','drink_id','desert_id','quantity')
	stuff_list = []
	for choosen in choosen_stuff:
		stuff_list.append(choosen)
	return stuff_list

#TODO 
"""
Method delete order (only possible in first 5 mins)
"""









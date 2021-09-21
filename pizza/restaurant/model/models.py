from django.db import models #similar to SQLalchemy 
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)    
    pizza_name = models.CharField(max_length=200)
   
    def __str__(self): #function: looking up pizzas         
        return self.pizza_name        

    def __repr__(self): 
        return f"Pizza {self.pizza_id}, {self.pizza_name}"  
        #f: fortmat the return so that it retuns the variable        
         
class topping(models.Model):
    topping_id = models.AutoField(primary_key=True)    
    topping_name = models.CharField(max_length=200)
    topping_price = models.FloatField() 
    vegeterian = models.BooleanField()
    
    def __str__(self): 
        return self.topping_id

class pizza_toppings(models.Model):
    pizza_toppings_id = models.AutoField(primary_key=True)
    pizza_id = models.ForeignKey(pizza, on_delete=models.CASCADE)    #FK 
    topping_id = models.ForeignKey(topping, on_delete=models.CASCADE)   #FK  
    
    def __str__(self): 
        return self.pizza_toppings_id

class drink(models.Model):
    drink_id = models.AutoField(primary_key=True)    
    drink_name = models.CharField(max_length=200)
    drink_price = models.FloatField() 
    def __str__(self): 
        return self.drink_id


class desert(models.Model):
    desert_id = models.AutoField(primary_key=True)    
    desert_name = models.CharField(max_length=200)
    desert_price = models.FloatField() 
    def __str__(self): 
        return self.desert_id
# 

class menu_item(models.Model):
    menu_item_id = models.AutoField(primary_key=True)    
    pizza_id = models.ForeignKey(pizza, on_delete=models.CASCADE)    #FK 
    drink_id = models.ForeignKey(drink, on_delete=models.CASCADE)    #FK 
    desert_id = models.ForeignKey(desert, on_delete=models.CASCADE)    #FK 
    quantity = models.IntegerField(default=0) 
    def __str__(self): 
        return self.menu_item_id

class address(models.Model):
    address_id = models.AutoField(primary_key=True)    
    postal_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house_number = models.IntegerField(default=0) 
    city = models.CharField(max_length=200)
    def __str__(self): 
        return self.address_id

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0) 
    discount_available = models.BooleanField(default=False)
    address_id = models.ForeignKey(address, on_delete= models.CASCADE)
    def __str__(self): 
        return self.customer_id


class orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)    #FK 
    #address_id = GenericForeignKey(customer)  FK
    total_price = models.FloatField(default=0) #calculated from drink, desert and pizza 
    total_discount= models.FloatField(default=0) # get boolean from costumer 
    order_time = models.DateTimeField('orderedTime')
    order_status = models.CharField(max_length=200) # only 3 options, cancelled/progress/out  #CHANGE https://riptutorial.com/django/example/30649/foreignkey
    def __str__(self):
        return self.order_id

class order_line(models.Model):
    order_line_id = models.AutoField(primary_key=True)    
    menu_item_id = models.ForeignKey(menu_item, on_delete=models.CASCADE)    #FK 
    quantity = models.IntegerField(default=0) 
    order_id = models.ForeignKey(orders, on_delete=models.CASCADE)    #FK 
    def __str__(self): 
        return self.menu_item_id


class employee(models.Model):
    employee_id = models.AutoField(primary_key=True)    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    area_code = models.CharField(max_length=200)
    
    def __str__(self): 
        return self.employee_id

class delivery(models.Model):
    order_id = models.AutoField(primary_key=True)    
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)    #FK 
    status = models.CharField(max_length=200)
    time_when_deliverer_left = models.DateTimeField('orderedTime')
    
    def __str__(self): 
        return self.employee_id


    

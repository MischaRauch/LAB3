from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)    
    pizza_name = models.CharField(max_length=200)
    def __str__(self): #function: looking up pizzas 
        return self.pizza_name

class Pizza_toppings(models.Model):
    pizza_toppings_id = models.AutoField(primary_key=True)
    pizza_id = models.IntegerField(default=0)    #FK 
    topping_id = models.IntegerField(default=0)   #FK  




class Drink(models.Model):
    drink_id = models.AutoField(primary_key=True)    
    drink_name = models.CharField(max_length=200)
    drink_price = models.FloatField() 
    def __str__(self): 
        return self.drink_name

class Desert(models.Model):
    desert_id = models.AutoField(primary_key=True)    
    desert_name = models.CharField(max_length=200)
    desert_price = models.FloatField() 
    def __str__(self): 
        return self.desert_name

class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer_id = models.IntegerField(default=0) #  FK 
    address = models.CharField(max_length=200) # FK
    total_price = models.FloatField() #calculated from drink, desert and pizza 
    total_discount= models.FloatField() # costumer 
    order_time = models.DateTimeField('orderedTime')
    order_status = models.CharField(max_length=200) # only 3 options, cancelled/progress/out 

    def __str__(self):
        return self.order_id

class Order_Pizza(models.Model):
    pizza_id = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)



    

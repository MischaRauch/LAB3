from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)    
    pizza_name = models.CharField(max_length=200)
    def __str__(self): #function: looking up pizzas 
        return self.pizza_name


class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer_id = models.IntegerField(default=0) # must be a FK later
    order_time = models.DateTimeField('orderedTime')
    order_status = models.CharField(max_length=200)

    def __str__(self):
        return self.order_id

class Order_Pizza(models.Model):
    pizza_id = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)



    

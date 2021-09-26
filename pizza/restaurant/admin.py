from django.contrib import admin

# Register your models here.
from restaurant.model.models import pizza, orders, topping, pizza_toppings, drink, desert, address, customer, employee, delivery, order_item

admin.site.register(pizza)
admin.site.register(topping)
admin.site.register(pizza_toppings)
admin.site.register(drink)
admin.site.register(desert)
admin.site.register(address)
admin.site.register(customer)
admin.site.register(employee)
admin.site.register(delivery)
admin.site.register(orders)
admin.site.register(order_item)

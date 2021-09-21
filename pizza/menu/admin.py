from django.contrib import admin

# Register your models here.
from .models import pizza, orders
admin.site.register(pizza)
admin.site.register(orders)

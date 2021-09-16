from django.contrib import admin

# Register your models here.
from .models import Pizza, Orders
admin.site.register(Pizza)
admin.site.register(Orders)

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Shipping_Address)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)
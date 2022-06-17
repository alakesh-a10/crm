
from django.contrib import admin

from .models import customer, order, products,tag

# Register your models here.

admin.site.register(customer)
admin.site.register(products)
admin.site.register(order)
admin.site.register(tag)

from django.contrib import admin
from .models import Product, Order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name','product_image', 'product_price', 'uuid']


class AdminOrder(admin.ModelAdmin):
    list_display = ['user','product', 'order_id', 'pay_response', 'is_paid']

admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
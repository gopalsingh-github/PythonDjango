from django.db import models
from django.contrib.auth.models import User
# Create your models here.

import uuid
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='upload/products')
    product_price = models.IntegerField()
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=500)
    pay_response = models.TextField(null=True)
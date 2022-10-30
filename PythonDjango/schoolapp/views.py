from django.shortcuts import render
from .models import Product, Order
# Create your views here.
import random
from django.conf import  settings
from instamojo_wrapper import Instamojo

api = Instamojo(api_key='8978b70bfd09d0345512e028c1ce0999', auth_token='afa50b4162a98aefd6faf6b2b64e163e', endpoint='https://test.instamojo.com/api/1.1/')

def home(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')



def signup(request):
    return render(request, 'signup.html')

def product(request):
    if request.method=="GET":
        product_data = Product.objects.all()
        product = {'products': product_data}
        return render(request, 'product.html', product)

def order(request, product_id):
    product_obj = Product.objects.get(uuid=product_id)
    response = api.payment_request_create(
        amount=product_obj.product_price,
        purpose='order process',
        buyer_name='gopal',
        email="gopaldugariya07@gmail.com",
        redirect_url="http://127.0.0.1:8000/order_success"
    )
    print('response',response)
    order_id = random.randint(1000, 9999)
    # order_data = Order.objects.create(user=request.user, product=product_obj, is_paid=False, order_id=order_id)
    # order_data.save()
    # product_in_order = Order.objects.get(order_id =order_id)
    data = {'product_in_order':product_obj.product_name, 'product_price': product_obj.product_price,
            'product_image':product_obj.product_image}
    return render(request, 'order.html', data)

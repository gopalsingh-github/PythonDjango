from django.shortcuts import render
from .models import Product, Order
# Create your views here.
import random
from django.conf import  settings
from instamojo_wrapper import Instamojo
from rest_framework.views import APIView, View
from rest_framework.response import Response


api = Instamojo(api_key='8978b70bfd09d0345512e028c1ce0999', auth_token='afa50b4162a98aefd6faf6b2b64e163e', endpoint='https://test.instamojo.com/api/1.1/')

def home(request):
    return render(request, 'login.html')

def login(request):
    print('ghhg')
    return render(request, 'login.html')

class LoginView(APIView):
        def get(self, request, format=None):
            print('get called ')
            context ={'msg':'success'}
            return Response(context)
        def post(self, request):
            print('post called')
            context ={'msg':'success'}
            return Response(context)


def signup(request):
    return render(request, 'signup.html')

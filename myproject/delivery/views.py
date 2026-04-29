from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer
# Create your views here.

def say_hello(request):
    # return HttpResponse("Say Hello my app is working")
    return render(request, 'index.html')

def Open_signup(request):
    return render(request, 'signup.html')

def Open_signin(request):
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            try:
                Customer.objects.get(username = username)
                return HttpResponse("Duplicate username!")
            except:
                Customer.objects.create(
                username = username,
                password = password,
                email = email,
                mobile = mobile,
                address = address,
            )
    return render(request, 'signin.html')           

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

    try:
        Customer.objects.get(username = username)
        if username == 'admin':
           return render(request, 'admin_home.html')
        else:
           return render(request, 'customer_home.html')
           
       
    except Customer.DoesNotExist:
        return render(request, 'fail.html')
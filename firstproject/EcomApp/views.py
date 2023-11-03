from django.shortcuts import render, redirect
from EcomApp.models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password



# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(email = email).exists():
            return HttpResponse("Email Already registered !")
        elif User.objects.filter(phone=phone).exists():
            return HttpResponse("Phone number already registered")
        else:
            User.objects.create(name=name, email = email, phone = phone, password=password)
            return HttpResponse("User created successfully!")

def table(request):
    data = User.objects.all
    return render(request, "table.html", {"data":data})        

def user_delete(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('/table/')
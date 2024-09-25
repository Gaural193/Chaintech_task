from django.shortcuts import render
from datetime import datetime
from .models import *
import random

def index(request):
    current_datetime = datetime.now()  
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "The purpose of our lives is to be happy.",
        "Life is what happens when you're busy making other plans."
    ]
    random_quote = random.choice(quotes)  
    context = {
        'random_quote': random_quote,
        'current_datetime': current_datetime,  
    }
    return render(request, 'index.html',context)

def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        city = request.POST['city']
        email = request.POST['email']
        phone= request.POST['phone']
        data=Userdata.objects.create(name=name,email=email,phone=phone,city=city,gender=gender,dob=dob)
        
        data.save()
    return render(request,"form.html")


def data(request):
    all_data = Userdata.objects.all()
    context = {'data' : all_data }
    return render(request,'data.html',context)


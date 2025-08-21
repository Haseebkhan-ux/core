
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'abdul haseeb', 'age': 21},
        {'name': 'nouman arshad', 'age': 20},
        {'name': 'ahmad nishat', 'age': 19},
    ]
    for people in peoples:
        if people['age'] :
         print("Yes")
    
    vegetables = ['Pumpkin', 'Tomato', 'potato']


    return render(request,"home/index.html", context={'Page' : 'Django 2023 Tutorial','peoples': peoples, 'vegetables': vegetables})

def about(request):
    context = {'Page' : 'About'}
    return render(request,"home/about.html" , context)

def contact(request):
    context = {'Page' : 'Contact'}
    return render(request,"home/contact.html" , context)

def success_page(request):
    print("*" * 10)
    context = {'Page' : 'Contact'}


    return HttpResponse("<h1>Hey this is a success page.</h1>")
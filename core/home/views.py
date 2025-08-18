from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request,'home/home.html')



def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a success page.</h1>")
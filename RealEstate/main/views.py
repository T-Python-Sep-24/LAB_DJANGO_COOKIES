from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_view(request):
    return render(request,"main/home_page.html")


def properties_view(request):
    return render(request,"main/properties.html")

def contact_view(request):
    return render(request,"main/contact_page.html")


def mode_view(request:HttpRequest,mode):
    
    response= redirect(request.GET.get("current","/"))

    if mode=='light':
        response.set_cookie('mode','light')
        
    
    elif mode=='dark':
        response.set_cookie('mode','dark')

    return response
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_page(request:HttpRequest):
    return render(request,'main/home.html')

def properties_page(request:HttpRequest):
    return render(request,'main/properties.html')


def contact_page(request:HttpRequest):
    return render(request,'main/contact.html')


def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse


# Create your views here.
def home_view(request:HttpRequest):

    return render(request,"main/home.html")


def properties_view(request: HttpRequest):
    properties = [
      
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "static/image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    
    ]

    request = render(request, 'main/properties.html', context={'properties': properties})

    return request


def contact_view(request: HttpRequest):
    request = render(request,'main/contact.html')
    return request


def dark_mode(request: HttpRequest):
    request = redirect('main:home_view')
    request.set_cookie("mode", "dark", max_age=60*60*24)

    return request

def light_mode(request: HttpRequest):
    request = redirect('main:home_view')
    request.delete_cookie("mode")

    return request


def services_view(request: HttpRequest):
    request = render(request, "main/services.html")

    return request

def about_view(request: HttpRequest):
    request = render(request, "main/about.html")

    return request
from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from django.conf.urls.static import static
# Create your views here.
def home(request : HttpRequest):
    return render(request , 'main/home.html')

def contact(request:HttpRequest):
    return render(request , 'main/contact.html')

def properties(request:HttpRequest)->render:
        properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
        response=render(request , 'main/properties.html',{'properties':properties})
        return response
def dark_mode(request:HttpRequest)->render:
     response=redirect("main:home")
     response.set_cookie("dark_mode","true")
     return response

def light_mode(request:HttpRequest)->render:
     response=redirect("main:home")
     response.set_cookie("dark_mode","false")
     return response
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home_view(request: HttpRequest):
    return render(request, "cooky/home.html")

def property_view(request: HttpRequest):
    return render(request, "cooky/property.html")

def contact_view(request: HttpRequest):
    return render(request, "cooky/contact.html")

def dark_view(request: HttpRequest):
    response = redirect("cooky:home_view")
    response.set_cookie("mode", "dark", max_age=60)
    return response
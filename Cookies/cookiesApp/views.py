from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.



def main_view(request:HttpRequest):
    request = render(request, 'main.html')
    return request

def properties_view(request:HttpRequest):

    request = render(request, 'properties.html')
    return request

def contact_view(request:HttpRequest):

    request = render(request, 'contact.html')
    return request

def dark_mode(request:HttpRequest):
    request = redirect("{% url 'cookiesApp:main_view' %}")
    request.set_cookie("mode", "dark")
    return request


def services_view(request:HttpRequest):
    request = render(request, "services.html")

    return request

def about_view(request:HttpRequest):
    request = render(request, "about.html")

    return request

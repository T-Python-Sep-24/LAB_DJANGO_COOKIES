from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.


def main_view(request:HttpRequest):
    request = render(request, 'main.html')
    return request


def properties_view(request: HttpRequest):
    properties = [
        {"title": "Villa Modern in Malqa", "url": "images/villa1.jpg"},
        {"title": "Great home for you in Rimal", "url": "/images/villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "url": "images/villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "url": "images/villa4.jpg"},
    ]
    request = render(request, 'properties.html', context={'properties': properties})
    return request


def contact_view(request: HttpRequest):

    request = render(request, 'contact.html')
    return request


def dark_mode(request: HttpRequest):
    request = redirect('cookiesApp:main_view')
    request.set_cookie("mode", "dark", max_age=60*60*24)
    print(request.cookies)
    return request

def light_mode(request: HttpRequest):
    request = redirect('cookiesApp:main_view')
    request.delete_cookie("mode")
    print(request.cookies)
    return request


def services_view(request: HttpRequest):
    request = render(request, "services.html")

    return request

def about_view(request: HttpRequest):
    request = render(request, "about.html")

    return request

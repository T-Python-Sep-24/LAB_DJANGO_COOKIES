from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def main(request: HttpRequest) :
    return render(request, 'main/main.html')

def properties_view(request: HttpRequest) :
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {'properties': properties})

def contact_view(request: HttpRequest) :
    return render(request, 'main/contact.html')

def dark_mode(request: HttpRequest) :
    response = redirect(request.META.get('HTTP_REFERER', 'main:main')) 
    response.set_cookie('dark_mode', 'true', max_age=30 * 24 * 60 * 60)  
    return response

def light_mode(request: HttpRequest) :
    response = redirect(request.META.get('HTTP_REFERER', 'main:main'))  
    response.set_cookie('dark_mode', 'true', max_age=-3600) 
    return response
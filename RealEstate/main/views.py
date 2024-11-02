from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.

properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    

def index_view(request):
    
    return render(request, "main/index.html")

def properties_view(request:HttpRequest):
    
    return render(request, "main/properties.html", {'properties': properties})

def contact_view(request:HttpRequest):
    
    return render(request, "main/contact.html")

def mode_view(request, mode):
    # Redirect to the previous page or home if there's no referrer
    response = redirect(request.GET.get("next", "/"))

    # Set the mode cookie to either "light" or "dark"
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")

    return response

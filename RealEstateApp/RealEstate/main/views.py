from django.shortcuts import render, redirect
from django.http import HttpRequest

#Home page
def mainView(request: HttpRequest):
    return render(request, "main/home.html")

#Property page
def propertyView(request: HttpRequest):

    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]

    return render(request, "main/property.html", context={"properties" : properties})

#Contact us page
def contactView(request: HttpRequest):
    return render(request, "main/contact.html")

#Mode change
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
    return response
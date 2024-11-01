from django.shortcuts import render, redirect
from django.http import HttpRequest

#Home page
def mainView(request: HttpRequest):
    return render(request, "main/home.html")

#Property page
def propertyView(request: HttpRequest):
    return render(request, "main/property.html")

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
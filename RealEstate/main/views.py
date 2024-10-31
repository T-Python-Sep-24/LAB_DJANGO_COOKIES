from django.shortcuts import render
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
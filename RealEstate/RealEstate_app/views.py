from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def main_page(request:HttpRequest):
    return render(request,"RealEstate_app\main_page.html")

def properties_page(request:HttpRequest):
    return render(request,"RealEstate_app\properties_page.html")

def contactUs_page(request:HttpRequest):
    return render(request,"RealEstate_app\contactUs_page.html")





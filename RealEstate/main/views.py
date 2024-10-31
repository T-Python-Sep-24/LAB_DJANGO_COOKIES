from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def main_view(request:HttpRequest):

    return render(request, "main/home.html")



def propertie_view(request:HttpRequest):

    return render(request, "main/properties.html")



def contact_view(request:HttpRequest):

    return render(request, "main/contact.html")
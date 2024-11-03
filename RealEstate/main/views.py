from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpRequest , HttpResponse 


def home_light_view(request:HttpRequest):
    
    # return render(request ,"main/homelight.html")
    response1 = render(request, 'main/homelight.html')
    response1.set_cookie('mode', 'light', max_age=60*60*24*7)  # Cookie expires in 7 days
    return response1

def home_dark_view(request:HttpRequest):

    # return render(request , "main/homedark.html")
    response = render(request, 'main/homedark.html')  # You can change this if you have a specific dark mode template
    response.set_cookie('mode', 'dark', max_age=60*60*24*7)
    return response
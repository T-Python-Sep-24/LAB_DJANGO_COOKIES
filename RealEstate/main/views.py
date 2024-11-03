from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpRequest , HttpResponse 
def home_view(request:HttpRequest):
    return render(request , 'main/home.html')


def home_light_view(request:HttpRequest):
    
    response = redirect('main:home_view')
    response.set_cookie('mode', 'light', max_age=-23324)  # Cookie expires in 7 days
    return response

def home_dark_view(request:HttpRequest):

    # return render(request , "main/homedark.html")
    response = redirect('main:home_view')  # You can change this if you have a specific dark mode template
    response.set_cookie('mode', 'dark', max_age=60*60*24*7)
    return response

def properties_view(request:HttpRequest):
     properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
     return render(request, "main/properties.html", context={"properties" : properties})


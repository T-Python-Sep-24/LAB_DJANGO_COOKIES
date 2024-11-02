# myapp/views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest


def contact_view(request: HttpRequest):
    return render(request, 'myapp/contact.html')

def mode_view(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response

def test_params_view(request: HttpRequest, param1, param2):
    return render(request, "myapp/test_params.html", {"param1": param1})


# myapp/views.py
from django.shortcuts import render

# Properties list data
properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]

def home_view(request):
    return render(request, 'myapp/home.html')

def properties_list_view(request):
    context = {'properties': properties}
    return render(request, 'myapp/properties_list.html', context)



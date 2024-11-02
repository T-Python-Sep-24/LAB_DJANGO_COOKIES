from django.shortcuts import render, redirect

# Sample data for properties
properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]

def home(request):
    return render(request, 'main/home.html', {'properties': properties})

def properties_view(request):
    return render(request, 'main/properties.html', {'properties': properties})

def set_dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', 'home'))
    response.set_cookie('mode', 'dark', max_age=60*60*24)  # 1-day cookie
    return response

def set_light_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', 'home'))
    response.delete_cookie('mode')
    return response

def contact(request):
    return render(request, 'main/contact.html')

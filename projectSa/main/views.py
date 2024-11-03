from django.shortcuts import render


def view_main(request):
    return render(request, 'main/main.html')

def view_properties(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html',{'properties': properties})
def view_contact(request):
    return render(request, 'main/contact.html')

def view_dark(request):
    return render(request, 'main/dark.html')

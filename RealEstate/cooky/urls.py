from django.urls import path
from . import views

app_name = "cooky"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("properties/", views.property_view, name="property_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("mode/dark/", views.dark_view, name="dark_view"),
    path("mode/light/", views.light_view, name="light_view")
]
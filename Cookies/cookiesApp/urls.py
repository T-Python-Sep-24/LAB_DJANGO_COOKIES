from django.urls import path
from . import views

app_name = "cookiesApp"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("properties/", views.properties_view, name="properties_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("services/", views.contact_view, name="services_view"),
    path("about/", views.contact_view, name="about_view"),

]
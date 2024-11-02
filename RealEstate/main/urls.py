from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("properties/", views.propertie_view, name="propertie_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("mode/<mode>/", views.mode_view, name="mode_view"),


]
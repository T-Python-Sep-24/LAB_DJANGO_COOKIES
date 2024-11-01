from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.mainView, name="mainView"),
    path("property/", views.propertyView, name="propertyView"),
    path("contact/", views.contactView, name="contactView"),
    path("mode/<mode>/", views.modeView, name="modeView"),
]
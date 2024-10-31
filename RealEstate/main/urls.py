from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.mainView, name="mainView"),
    path("", views.propertyView, name="propertyView"),
    path("", views.contactView, name="contactView"),
]
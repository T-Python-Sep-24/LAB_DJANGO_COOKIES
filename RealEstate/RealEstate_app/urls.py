from . import views
from django.urls import path 

app_name = "RealEstate_app"
urlpatterns = [
   path("", views.main_page_page, name="main_page"),
   path("properties/", views.properties_page_page, name="properties_page"),
   path("contact/", views.contactUs_page_page, name="contactUs_page"),
]



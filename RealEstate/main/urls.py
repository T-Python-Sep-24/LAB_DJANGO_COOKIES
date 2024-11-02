from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.properties_view, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('dark_mode/', views.set_dark_mode, name='set_dark_mode'),
    path('light_mode/', views.set_light_mode, name='set_light_mode'),
]

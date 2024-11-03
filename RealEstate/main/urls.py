from django.urls import path
from .views import home, properties_view, services, about, contact, signup

urlpatterns = [
    path('', home, name='home'),
    path('properties/', properties_view, name='properties'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
]

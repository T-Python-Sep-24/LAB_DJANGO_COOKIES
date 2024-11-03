from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home_view'), 
    path('set-mode/', views.set_mode_view, name='set_mode'),  
    path('properties/',views.properties_view,name='properties_view'),
    path('contact/',views.contact_view , name="contact_view")
]

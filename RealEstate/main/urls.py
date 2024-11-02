from django.contrib import admin
from django.urls import path
from main import views

app_name = "main"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),  
    path('properties/', views.properties_view, name='properties_view'), 
    path('contact/', views.contact_view, name='contact_view'), 
    path('dark-mode/', views.dark_mode, name='dark_mode'),
    path('light-mode/', views.light_mode, name='light_mode'),


]

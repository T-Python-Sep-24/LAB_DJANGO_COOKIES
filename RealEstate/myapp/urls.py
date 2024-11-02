from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('properties_list/', views.properties_list_view, name='properties_list'),
    path('contact/', views.contact_view, name='contact'),
    path('mode/<str:mode>/', views.mode_view, name='mode_view'),  
]

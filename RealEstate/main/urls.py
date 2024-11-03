from django.urls import path
from . import views 

app_name = "main"
# راح ارجعله 
urlpatterns = [


    path('',views.home_view , name='home_view'),
    path('home/light',views.home_light_view , name="home_light_view" ),
    path('home/dark',views.home_dark_view , name='home_dark_view'),
    path('properties/',views.properties_view , name='properties_view'),
    
]

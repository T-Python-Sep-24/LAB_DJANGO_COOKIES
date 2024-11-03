from django.urls import path
from . import views 

app_name = "main"
# راح ارجعله 
urlpatterns = [
    path('',views.home_light_view , name='home_light_view'),
    path('home/dark',views.home_dark_view , name='home_dark_view')
    
]

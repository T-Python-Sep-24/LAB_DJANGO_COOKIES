from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_main, name='index'),
    path('properties/',views.view_properties, name='properties'),
    path('contact/',views.view_contact, name='contact'),
    path('dark/',views.view_dark, name='dark'),
]

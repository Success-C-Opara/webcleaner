from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('dash/', views.dash, name="dash"),
    path('fill/', views.fill, name="fill"),
   
]
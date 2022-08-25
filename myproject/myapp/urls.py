from django.contrib import admin
from django.urls import path
from . import views 

app_name="myapp"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('detail/<int:id>/', views.detail, name="details"),
    path('update/<int:id>/', views.update, name="update"),
]

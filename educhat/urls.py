from django.contrib import admin
from django.urls import path
from educhat import views

urlpatterns = [
    path("", views.index, name="home"),
    path("chat", views.chat, name="chat"),  
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard")
]
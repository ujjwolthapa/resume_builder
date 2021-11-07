from django import http
from django.urls import path
from .import views

from django.http.response import HttpResponse



urlpatterns = [
    path('',views.Home,name="home"),
    path('login',views.LoginPage,name="login"),
    path('logout',views.LogoutUser,name="logout"),
    path('dashboard',views.DashboardPage,name="dashboard"),
    path('register',views.RegisterPage,name="register"),
    path('cv-form/<str:pk>',views.CvFormPage,name="cv-form")
]

from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 
urlpatterns = [
    path('',views.index,name="apindex"),
    path('register',views.create_auth,name='api_register'),
    path('login',obtain_auth_token,name='login'),
]

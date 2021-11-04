from django.contrib.auth import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CvForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
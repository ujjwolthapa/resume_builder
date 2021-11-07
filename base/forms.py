from django.contrib.auth import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CvForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','job_title','phoneNumber','email','instagram','location','about','avatar']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
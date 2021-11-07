from django.contrib.auth import models
from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CvForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','job_title','phoneNumber','email','instagram','location','about','avatar']
        
    def __init__(self, *args, **kwargs):
        super(CvForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
        
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    
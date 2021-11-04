from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django import forms
from .forms import MyUserCreationForm
from .models import User,Education,Experience,Skill
from django.contrib import messages
# Create your views here.

def CvForm(request):
    return render(request,'cv-form.html')


def Home(request):
    return render(request,'home.html')

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request,'username doesnt found')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'password is wrong')
        
    return render(request,'login.html')

def LogoutUser(request):
    logout(request)
    return redirect('home')

def RegisterPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'An eroor have occured')
    return render(request,'register.html',{'form':form})

def DashboardPage(request):
    return render(request,'dashboard.html')
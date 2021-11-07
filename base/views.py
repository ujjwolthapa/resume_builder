from django.contrib.auth import authenticate,login,logout
from django.db import reset_queries
from django.shortcuts import redirect, render
from django import forms
from .forms import MyUserCreationForm,CvForm
from .models import User,Education,Experience,Skill
from django.contrib import messages
# Create your views here.

def CvFormPage(request,pk):
    user = User.objects.get(id=request.user.id)
    form = CvForm(instance=request.user)
  
    skills = user.skill_set.all()
    educations = user.education_set.all()
    experiences = user.experience_set.all()
    context ={'form':form,'skills':skills,'educations':educations,'experinces':experiences}



    if request.method == 'POST':
        form = CvForm(request.POST,request.FILES,instance=request.user)
        skill_name = request.POST.get('skill')
        
        if form.is_valid():
            form.save()
            skills_name = request.POST.getlist("skill")
            education_name = request.POST.getlist("education")
            timestart = request.POST.getlist("timestart")
            timeend = request.POST.getlist("timeend")
            experience_name = request.POST.getlist("experience")
            etimestart = request.POST.getlist("etimestart")
            etimeend = request.POST.getlist("etimeend")
            # print(name)
            for i in range(len(request.POST.getlist('skill'))):
                Skill.objects.get_or_create(
                    User=request.user,
                    
                    name = skills_name[i]
                )
            for i in range(len(request.POST.getlist("education"))):
                Education.objects.get_or_create(
                    User = request.user,
                    name = education_name[i],
                    timestart = timestart[i],
                    timeend = timeend[i]
                    

                )
            for i in range(len(request.POST.getlist("experience"))):
                Experience.objects.get_or_create(
                    User = request.user,
                    name = experience_name[i],
                    timestart = etimestart[i],
                    timeend = etimeend[i]

                )
            return redirect('home')
        else:
            messages.error(request,'form error occured check if country code is added in phone and picture is selected')
        
    return render(request,'cv-form.html',context)


def Home(request):
    return render(request,'home.html')

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request,'username doesnt found')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
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
            return redirect('home')
        else:
            messages.error(request,'An error have occured')
    return render(request,'register.html',{'form':form})

def DashboardPage(request):
    return render(request,'dashboard.html')
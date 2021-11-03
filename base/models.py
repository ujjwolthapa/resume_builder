from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200,null=True,blank=False)
    job_title = models.CharField(max_length=200,null=True,blank=False)
    phoneNumber = PhoneNumberField(null = True, blank = False)
    email = models.EmailField(null=True)
    instagram = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200,null=True)
    about = models.TextField(max_length=200,null=True)
    avatar = models.ImageField(null=True,default="avatar.svg")
    REQUIRED_FIELDS = []


class Skill(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        self.name

class Experience(models.Model):
    User = models.ForeignKey(User,on_delete=CASCADE)
    name = models.CharField(max_length=200,null=True)
    timestart = models.DateField(null=True)
    timeend = models.DateField(null=True)

    def __str__(self):
        self.name

class Education(models.Model):
    User = models.ForeignKey(User,on_delete=CASCADE)
    name = models.CharField(max_length=200,null=True)
    timestart = models.DateField(null=True)
    timeend = models.DateField(null=True)

    def __str__(self):
        self.name




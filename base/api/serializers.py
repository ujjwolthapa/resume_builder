from django.contrib.auth.backends import UserModel
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from base.models import User


class UserSerializer(ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ["username","password","password2"]
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        account = User(
            username = self.validated_data['username']

        )
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password1 != password2:
            raise serializers.ValidationError({'password':'password mist match'})
        account.set_password(password1)
        account.save()
        return account
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from datetime import datetime
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from base.models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m%Y %H:%M:%S")
    message = 'server is live current time is'
    return Response(data=message + date, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_auth(request):
    serializer = UserSerializer(data=request.data)
    data ={}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "sucessfully registered "
        data['username'] = account.username
        token = Token.objects.get(user=account).key
        data['token'] = token
        return Response(data)
    else:
        data = serializer.errors
        return Response(data)
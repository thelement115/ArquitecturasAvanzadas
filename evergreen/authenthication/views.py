from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from . import serializers
from . import models


# Create your views here.

class SingUp(viewsets.ModelViewSet):
    queryset = models.UserExtraInfo.objects.all()
    serializer_class = serializers.UserExtraInfoSerializer


class LoginViewSet(viewsets.ViewSet):
    """ check username and password and return an auth token """

    serializer_class = AuthTokenSerializer
    
    def create(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            return ObtainAuthToken().post(request)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

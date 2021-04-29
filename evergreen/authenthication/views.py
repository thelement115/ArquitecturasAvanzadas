from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


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
            user = authenticate(username=request.data['username'], password=request.data['password'])
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                })
            else:
                return Response({"status_code": 405, "detail": "UNAUTHORIZED"})
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

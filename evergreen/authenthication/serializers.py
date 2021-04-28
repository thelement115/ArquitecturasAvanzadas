from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = models.User(**validated_data, is_active=True)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        try:
            password = validated_data.pop('password')
            instance.set_password(password)
        except:
            pass
        return super(UserSerializer, self).update(instance, validated_data)


class UserExtraInfoSerializer(serializers.ModelSerializer):
    userId = UserSerializer(many = False)

    def create(self, validated_data):
        user = validated_data.pop('userId')
        serializer_aux = UserSerializer(data= user)
        if serializer_aux.is_valid():
            user = serializer_aux.save()
            userExtra = models.UserExtraInfo(**validated_data)
            userExtra.userId = user
            userExtra.save()
            return userExtra

    class Meta:
        model = models.UserExtraInfo
        fields = '__all__'
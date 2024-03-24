from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    
class UserSigninSerialize(serializers.Serializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)
    
    def username_exists(self, username):
        return User.objects.filter(username=username).exists()


class UserLoginSerialize(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']

    def check_user(self, clean_data):
        user = authenticate(username=clean_data['username'], password=clean_data['password'])
        if not user:
            raise 'user not found'
        return user
     
       
    
        
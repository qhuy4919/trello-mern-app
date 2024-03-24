from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

from .serializers import UserLoginSerialize, UserSigninSerialize
from .models import User

@api_view(['POST'])
@csrf_exempt
def UserSignup(request):
    serializer = UserSigninSerialize(data=request.data)

    if serializer.is_valid(raise_exception=True):
        try:
            if serializer.username_exists(request.data['username']):
                return Response(
                'User existed', 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            user = serializer.create(request.data)
            print('user: ', user)
            token = Token.objects.create(user=user)
            print('token: ', token)
            
            if user and token: 
                return Response({
                'token': token.key,
                'user': request.data
            }, status=status.HTTP_200_OK)
        except: 
            return Response(
                'Signin Failed', 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
      
        
        
        
        
@api_view(['POST'])
@csrf_exempt
def UserLogin(request):
    data = request.data
    print('data: ', data)
    serializer = UserLoginSerialize(data=data)
    if serializer.is_valid(raise_exception=True):
        print(serializer)
        user = serializer.check_user(data)
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        return Response({
                'token': token.key,
                '_created': created,
                'user': serializer.data['username'],  
            })
    return Response('Not found', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def UserLogout(request):
    if request.user.is_authenticated:
        request.user.auth_token.delete()    
        logout(request)
    
    return Response('Logout successful',status=status.HTTP_200_OK)


    
    
    
    
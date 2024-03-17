from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout

from .serializers import UserLoginSerialize, UserSigninSerialize
from .models import User

@api_view(['POST'])
def UserSignup(request):
    serializer = UserSigninSerialize(data=request.data)

    if serializer.is_valid(raise_exception=True):
        try:
            user = serializer.create(request.data)
            token = Token.objects.create(user=user)
            if user and token: 
                return Response({
                'token': token.key,
                'user': serializer.data['username'],
            }, status=status.HTTP_200_OK)
        except: 
            return Response(
                'Signin Failed', 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
      
        
        
        
        
@api_view(['POST'])
def UserLogin(request):
    data = request.data
    serializer = UserLoginSerialize(data=data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.check_user(data)
        login(request, user)
        # if not user.check_password(request.data['password']):
        #     return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                'token': token.key,
                '_created': created,
                'user': serializer.data['username'],  
            })
    return Response('Not found', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def UserLogout(request):
    logout(request)
    
    return Response('Logout successful',status=status.HTTP_200_OK)


    
    
    
    
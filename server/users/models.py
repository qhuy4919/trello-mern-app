from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, password: None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('User should have email')
        
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, username, email=None, password=None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('User should have email')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_supperuser = True
        user.save()
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(unique=True, db_index=True)
    email = models.EmailField(null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "username"
    
    objects = UserManager()
    
    

    

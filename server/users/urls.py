from django.urls import path

from . import views



urlpatterns = [
    path('signup', views.UserSignup),
    path('login', views.UserLogin),
    path('logout', views.UserLogout)
]



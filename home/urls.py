from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handeLogin,name='handleLogin'),
    path('logout', views.handelLogout, name="handleLogout"),
   
]

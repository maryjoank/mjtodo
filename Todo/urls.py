from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.com,name='contact'),
    path('register/',views.registerpage,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'), 
]
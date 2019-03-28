
from django.urls import path
from . import views
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.home, name = 'home'),
    #path('login/', login, {'template_name': 'registration/login.html'}),
    path("register/", views.register, name="register"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name ='login'),
    #path('login/chat/', views.chatwin, name ='chat'),


    path('', views.login_request, name ='login'),

]

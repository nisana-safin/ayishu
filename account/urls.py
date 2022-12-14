from django.urls import include,path

from account import views

urlpatterns = [
     path('register',views.register,name='register'),
     path('login', views.login, name='login'),
     path('logout', views.logout, name='logout'),
    ]
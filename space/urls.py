from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'space'
urlpatterns = [
    #Home Page
    path('', views.main, name='main'),
    #Page for Europa
    path('moon/', views.moon, name='moon'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
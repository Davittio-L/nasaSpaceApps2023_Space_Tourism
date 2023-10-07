from django.urls import path
from . import views

app_name = 'space'
urlpatterns = [
    #Home Page
    path('', views.main, name='main'),
    #Page for Europa
    path('moon/', views.moon, name='moon'),
]
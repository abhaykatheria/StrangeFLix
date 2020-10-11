from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('loggedin/', views.home, name="loggedin"),
    #path('/accounts', include('allauth.urls')),
]
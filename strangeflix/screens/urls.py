from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='ok'),
    path('loggedin/', views.loggedin, name="loggedin"),
    #path('/accounts', include('allauth.urls')),
]
from django.urls import path, include
from .views import (
    HomeView, WelcomeScreen,
    PriceView,
)

app_name = "screens"

urlpatterns = [
    #path('', welcome_screen,name='home'),
    path('', WelcomeScreen.as_view(), name="welcome"),
    path('loggedin/', HomeView.as_view(), name="loggedin"),
    path('price-list/', PriceView.as_view(), name="price"),
    #path('/accounts', include('allauth.urls')),
]
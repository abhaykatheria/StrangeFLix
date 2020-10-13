from django.urls import path, include
from .views import (
    HomeView, WelcomeScreen,
    PriceView, PaymentView,
    SelectPlanView
)

app_name = "screens"

urlpatterns = [
    #path('', welcome_screen,name='home'),
    path('', WelcomeScreen.as_view(), name="welcome"),
    path('loggedin/', HomeView.as_view(), name="loggedin"),
    path('price-list/', PriceView.as_view(), name="price"),
    path('planform/payment/', PaymentView.as_view(), name="payment"),
    path('planform/', SelectPlanView.as_view(), name="planform"),
    #path('/accounts', include('allauth.urls')),
]
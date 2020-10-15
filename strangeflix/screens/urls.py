from django.urls import path, include
from .views import (
    HomeView, WelcomeScreen,
    PriceView, PaymentView,
    SelectPlanView, MovieDetailView,

    payment_complete,
)

app_name = "screens"

urlpatterns = [
    #path('', welcome_screen,name='home'),
    path('', WelcomeScreen.as_view(), name="welcome"),
    path('loggedin/', HomeView.as_view(), name="loggedin"),
    path('price-list/', PriceView.as_view(), name="price"),
    path('planform/payment/', PaymentView.as_view(), name="payment"),
    path('payment-complete/', payment_complete, name="payment_complete"),
    path('planform/', SelectPlanView.as_view(), name="planform"),
    #path('/accounts', include('allauth.urls')),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]
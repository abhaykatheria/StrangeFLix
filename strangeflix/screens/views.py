from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie
from django.views.generic import TemplateView, ListView, DeleteView
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Movie
    template_name = "home.html"


class WelcomeScreen(TemplateView):
    template_name = "welcome.html"


class PriceView(TemplateView):
    template_name = "price.html"
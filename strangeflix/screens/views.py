from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie
from django.views.generic import TemplateView, ListView, DeleteView


class HomeView(ListView):
    model = Movie
    template_name = "home.html"

def home(request):
    context = {
        'items': Movie.objects.all()
    }
    return render(request, "home.html", context)


class WelcomeScreen(TemplateView):
    template_name = "welcome.html"
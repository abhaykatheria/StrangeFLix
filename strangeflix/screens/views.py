from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie
from django.views.generic import TemplateView, ListView, DeleteView
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DeleteView, DetailView


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Movie
    template_name = "home.html"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"


def home(request):
    context = {
        'items': Movie.objects.all()
    }
    return render(request, "home.html", context)


class WelcomeScreen(TemplateView):
    template_name = "welcome.html"


class PriceView(TemplateView):
    template_name = "price.html"
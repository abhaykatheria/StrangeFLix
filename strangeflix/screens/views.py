from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Plans, UserProfile
from django.views.generic import TemplateView, ListView, DeleteView
from django.utils.decorators import method_decorator
from .forms import SelectPlanForm
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

class SelectPlanView(ListView):
    def get(self, *args, **kwargs):
        #model = Plans.objects.all()
        form = SelectPlanForm()
        context = {
            'form': form,
        }
        return render(self.request,"planform.html", context)
    def post(self,*args, **kwargs):
        form = SelectPlanForm(self.request.POST)
        if form.is_valid():
            #print("for is valid")
            plan = get_object_or_404(Plans, plan_type=form.cleaned_data.get('plan_option'))
            # print(form.cleaned_data.get('plan_option'))
            # print(plan.plan_length)
            if self.request.user.is_anonymous is not True:
                userprofile = UserProfile.objects.get(user=self.request.user)
                userprofile.plan = plan
                userprofile.save()
                return redirect("screens:payment")
            else:
                return redirect("screens:planform")
        else:
            #print("form is not valid")
            return redirect("screens:planform")
        


class PaymentView(LoginRequiredMixin, TemplateView):
    template_name = "payment.html"
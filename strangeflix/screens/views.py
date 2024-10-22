from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Plans, UserProfile, Payment
from django.views.generic import TemplateView, ListView, DeleteView
from django.utils.decorators import method_decorator
from .forms import SelectPlanForm, PaymentForm, CommentForm, ProfileForm
from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from django.contrib import messages
from django.conf import settings
import json
import stripe
from django.db.models import Q
from datetime import datetime, timezone
from allauth.account.views import PasswordChangeView, PasswordSetView
# `source` is obtained with Stripe.js; see https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token

stripe.api_key = settings.STRIPE_SECRET_KEY





class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        success_url = 'http://127.0.0.1:8000/profile/' # <- choose your URL
        return success_url

class CustomPasswordSetView(LoginRequiredMixin, PasswordSetView):
    def get_success_url(self):
        success_url = 'http://127.0.0.1:8000/profile/' # <- choose your URL
        return success_url

date_format = "%Y-%m-%d"

def is_prime(self):
    userprofile = UserProfile.objects.get(user=self.request.user)
    if userprofile.plan is None or userprofile.plan_buy_date is None:
        return False
    user_date = datetime.strptime(str(userprofile.plan_buy_date.date()), date_format)
    my_date = datetime.strptime(str(datetime.now().date()), date_format) 
    delta = (my_date - user_date).days
    plan_length = userprofile.plan.plan_length
    print(delta)
    print(plan_length)
    if delta <= plan_length and userprofile.is_active_plan is True :
        return True
    else:
        userprofile.is_active_plan = False
        userprofile.save()
        return False
    


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    def get(self,*args,**kwargs):
        if is_prime(self):
            print("Prime user")
            context = {
                'object_list': Movie.objects.all(),
                'prime': True,
            }
        else:
            print("Not Prime user")
            context = {
                'object_list': Movie.objects.all(),
                'prime': False,
            }
        return render(self.request, "home.html", context)

@method_decorator(login_required, name='dispatch')
class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"



class SearchResultsView(ListView):
    model = Movie
    template_name = 'search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        res = Movie.objects.filter(
            Q(name__icontains=query) | Q(genre__icontains=query) | Q(director__icontains=query)| Q(actors__icontains=query)
        )
        return res

def home(request):
    context = {
        'items': Movie.objects.all()
    }
    return render(request, "home.html", context)
def s(request):
    context = {
        'items': Movie.objects.all()
    }
    return render(request,"s.html")

class WelcomeScreen(TemplateView):
    def get(self,*args,**kwargs):
        if self.request.user.is_anonymous is True:
            return render(self.request, "welcome.html")
        else:
            return redirect("screens:loggedin")


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
                print(self.request.user.username)
                userprofile = UserProfile.objects.get(user=self.request.user)
                userprofile.plan = plan
                userprofile.save()
                return redirect("screens:payment")
            else:
                return redirect("screens:planform")
        else:
            #print("form is not valid")
            return redirect("screens:planform")
        
def payment_complete(request):
    body = json.loads(request.body)
    print("BODY-->", body)
    userprofile = UserProfile.objects.get(user=request.user)
    payment = Payment(
        user = request.user,
        charge_id = body['payID'],
        amount = userprofile.plan.plan_price
    )
    payment.save()
    userprofile.is_active_plan = True
    userprofile.plan_buy_date = payment.timestamp
    userprofile.payment = payment
    userprofile.save()
    return redirect("profile")


class PaymentView(LoginRequiredMixin, TemplateView):
    def get(self, *args, **kwargs):
        userprofile = UserProfile.objects.get(user=self.request.user)
        if userprofile.plan.plan_type:
            context = {
                'amount': userprofile.plan.plan_price,
                'days': userprofile.plan.plan_length
            }
            return render(self.request, 'payment.html', context)
        else:
            return redirect("screens:planform")

    def post(self, *args, **kwargs):
        userprofile = UserProfile.objects.get(user=self.request.user)
        form = PaymentForm(self.request.POST)

        if form.is_valid():
            print("valid form")
            token = form.cleaned_data.get('stripeToken')
            amount = userprofile.plan.plan_price
            try:
                charge = stripe.Charge.create(
                    amount=amount,  # cents
                    currency="usd",
                    source=token
                )
                payment = Payment(
                    user = self.request.user,
                    charge_id = charge['id'],
                    amount = userprofile.plan.plan_price
                )
                payment.save()
                userprofile.is_active_plan = True
                userprofile.plan_buy_date = payment.timestamp
                userprofile.payment = payment
                userprofile.save()
                return redirect("screens:profile")
            except stripe.error.CardError as e:
                body = e.json_body
                err = body.get('error', {})
                print(err.get('message'))
                return redirect("screens:planform")
        else:
            return redirect("screens:planform")

def add_comment_to_post(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('screens:movie_detail', pk=movie.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


class ProfileView(LoginRequiredMixin,ListView):
    def get(self, *args, **kwargs):
        profile = UserProfile.objects.get(user=self.request.user)
        form = ProfileForm()
        context = {
            'profile': profile,
            'form': form
        }
        return render(self.request, "profile.html", context)
    def post(self, *args,**kwargs):
        form = ProfileForm(self.request.POST,self.request.FILES)
        if form.is_valid():
            print("valid")
            profile = UserProfile.objects.get(user=self.request.user)
            profile.image = form.cleaned_data["image"]
            profile.save()
        else:
            print("form not valid")
        return redirect("screens:profile")


class Enjoy():
    data = 3
    # testing only
    
from django.http import HttpResponse
from django.shortcuts import render


def loggedin(request):
    return HttpResponse("Aoo RAja")

def home(request):
    #return HttpResponse('<h1>GO BACK</h>')
    return render(request, 'home.html')
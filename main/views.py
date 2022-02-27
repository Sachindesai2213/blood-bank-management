from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *


# Create your views here.
@login_required(login_url='/login/')
def index_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'index.html', context)


def login_view(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'login.html', context)


def signup_view(request):
    blood_types = BloodType.objects.all()
    context = {
        'title': 'Registration',
        'blood_types': blood_types,
    }
    return render(request, 'signup.html', context)

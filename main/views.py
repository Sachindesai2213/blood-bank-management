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


@login_required(login_url='/login/')
def requirements(request):
    context = {
        'title': 'Home'
    }
    if request.path == '/requirements/me/':
        return render(request, 'requirements/me.html', context)
    return render(request, 'requirements/index.html', context)


@login_required(login_url='/login/')
def my_donations(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'donations/index.html', context)


@login_required(login_url='/login/')
def myprofile(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'my-profile.html', context)

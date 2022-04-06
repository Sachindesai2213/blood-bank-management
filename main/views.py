from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

from .models import *


# Create your views here.
@login_required(login_url='/login/')
def index_view(request):
    return redirect('/profile/')
    # context = {
    #     'title': 'Home'
    # }
    # return render(request, 'index.html', context)


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
    blood_types = BloodType.objects.all()
    user_requirements = list(Requirement.objects.filter(user=request.user).values('id', 'location', 'blood_type__abbr', 'quantity', 'description', 'date_time', 'requirement_fulfilled').order_by('-id'))
    global_requirements = list(Requirement.objects.all().exclude(user=request.user).values('id', 'location', 'blood_type__abbr', 'quantity', 'description', 'date_time', 'requirement_fulfilled').order_by('-id'))
    for requirement in user_requirements:
        requirement['date_time'] = requirement['date_time'].strftime('%d-%m-%Y %H:%M')
        requirement['requirement_fulfilled'] = 'Yes' if requirement['requirement_fulfilled'] else 'No'
    for requirement in global_requirements:
        requirement['date_time'] = requirement['date_time'].strftime('%d-%m-%Y %H:%M')
        requirement['requirement_fulfilled'] = 'Yes' if requirement['requirement_fulfilled'] else 'No'
    context = {
        'title': 'Home',
        'blood_types': blood_types,
        'user_requirements': user_requirements,
        'global_requirements': global_requirements,
    }
    return render(request, 'requirements.html', context)


@login_required(login_url='/login/')
def about_us_view(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'about-us.html', context)


@login_required(login_url='/login/')
def contact_us_view(request):
    context = {
        'title': 'Contact Us'
    }
    return render(request, 'contact-us.html', context)


@login_required(login_url='/login/')
def my_donations(request):
    donation_requests = list(RequirementDonors.objects.filter(donor=request.user).values('requirement__id', 'requirement__location', 'requirement__blood_type__abbr', 'requirement__quantity', 'requirement__description', 'requirement__date_time', 'requirement__requirement_fulfilled', 'acceptance_status', 'requirement__user__first_name', 'requirement__user__last_name', 'requirement__user__email').order_by('-requirement__id'))
    for donation_request in donation_requests:
        donation_request['requirement__date_time'] = donation_request['requirement__date_time'].strftime('%d-%m-%Y %H:%M')
        donation_request['requirement__requirement_fulfilled'] = 'Yes' if donation_request['requirement__requirement_fulfilled'] else 'No'
        donation_request['acceptance_status'] = 'Yes' if donation_request['acceptance_status'] else 'No'
    context = {
        'title': 'Home',
        'donation_requests': donation_requests,
    }
    return render(request, 'donations/index.html', context)


@login_required(login_url='/login/')
def profile_view(request):
    user = UserPersonalInfo.objects.get(user=request.user)
    blood_groups = BloodType.objects.all()
    context = {
        'title': 'Home',
        'user': user,
        'blood_groups': blood_groups,
    }
    return render(request, 'my-profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login/')


def donation_requests_view(request):
    donation_requests = list(RequirementDonors.objects.filter(requirement__user=request.user).values('id', 'requirement__id', 'requirement__location', 'requirement__blood_type__abbr', 'requirement__quantity', 'requirement__description', 'requirement__date_time', 'requirement__requirement_fulfilled', 'acceptance_status', 'requirement__user__first_name', 'requirement__user__last_name', 'requirement__user__email', 'donor__first_name').order_by('-requirement__id'))
    for donation_request in donation_requests:
        donation_request['requirement__date_time'] = donation_request['requirement__date_time'].strftime('%d-%m-%Y %H:%M')
        donation_request['requirement__requirement_fulfilled'] = 'Yes' if donation_request['requirement__requirement_fulfilled'] else 'No'
        donation_request['acceptance_status'] = 'Yes' if donation_request['acceptance_status'] else 'No'
    context = {
        'title': 'Home',
        'donation_requests': donation_requests,
    }
    return render(request, 'donation-requests.html', context)

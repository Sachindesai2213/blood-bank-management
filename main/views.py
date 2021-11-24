from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def index_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'index.html', context)


def login_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'login.html', context)

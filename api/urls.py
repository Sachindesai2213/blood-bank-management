from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('requirements/', requirement_view, name='requirements'),
    path('requirement-donors/', requirement_donors_view, name='requirements-donors'),
    path('requirement-donor/<int:id>/', requirement_donor_view, name='requirements-donor'),
]

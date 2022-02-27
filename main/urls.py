from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('requirements/', requirements, name='requirements'),
    path('requirements/me/', requirements, name='requirements'),
    path('my-donations/', my_donations, name='my-donations'),
    path('my-profile/', myprofile, name='my-profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

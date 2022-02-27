from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('', requirements, name='requirements'),
    path('requirements/me/', requirements, name='requirements'),
    path('my-donations/', my_donations, name='my-donations'),
    path('profile/', profile_view, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

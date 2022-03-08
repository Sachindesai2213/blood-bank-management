from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('requirements/', requirements, name='requirements'),
    # path('requirements/me/', requirements, name='requirements'),
    path('my-donations/', my_donations, name='my-donations'),
    path('profile/', profile_view, name='profile'),
    path('about-us/', about_us_view, name='about-us'),
    path('contact-us/', contact_us_view, name='contact-us'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

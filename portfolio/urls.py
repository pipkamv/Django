from django.urls import path
from.views import *

urlpatterns = [
    path('', index, name='home'),
    path('portfolio/contact.html', contact, name='contacts'),
    path('portfolio/about.html', about, name='about'),
]

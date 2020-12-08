from django.shortcuts import render
from .models import Portfolio


def index(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'index.html')

def contact(request):
    return render(request, template_name='portfolio/contact.html')

def about(request):
    return render(request, template_name='portfolio/about.html')


from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
import pytz

def get_common_context():
    """Return common context for all views"""
    return {
        'home_url': reverse('portfolio:home'),
        'about_url': reverse('portfolio:about'),
        'projects_url': reverse('portfolio:projects'),
        'contact_url': reverse('portfolio:contact')
    }

def home(request):
    context = get_common_context()
    return render(request, 'portfolio/home.html', context)

def about(request):
    context = get_common_context()
    return render(request, 'portfolio/about.html', context)

def projects(request):
    context = get_common_context()
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    context = get_common_context()
    return render(request, 'portfolio/contact.html', context)

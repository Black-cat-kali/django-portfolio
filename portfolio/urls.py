from django.urls import path
from . import views

app_name = 'portfolio'  # Add namespace for URL reversing

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    # path('time/', views.current_time, name='current_time'),
]
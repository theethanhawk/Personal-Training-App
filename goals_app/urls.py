"""Defines URL patterns for goals_app"""

from django.urls import path
from . import views

app_name = 'goals_app'
urlpatterns = [
    # Main dashboard
    path('', views.goalsHome, name='goals')
]
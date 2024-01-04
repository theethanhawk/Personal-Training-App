"""Defines URL patterns for goals_app"""

from django.urls import path
from . import views

app_name = 'goals_app'
urlpatterns = [
    # Main dashboard
    path('', views.goalsHome, name='goals'),
    # Dashboard for adding goals
    path('add_goals/', views.add_Goals, name='add_goals_dashboard'),
    # Dashboard for viewing goals
    path('goals_display_dashboard/', views.display_Goals, name='goals_display_dashboard'),
]
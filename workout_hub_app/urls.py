"""Defines URL patterns for workout_hub_app"""

from django.urls import path
from . import views

app_name = 'workout_hub_app'
urlpatterns = [
    # Workouts dashboard
    path('', views.workoutsHome, name='workouts')
]
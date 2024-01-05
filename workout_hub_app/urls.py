"""Defines URL patterns for workout_hub_app"""

from django.urls import path
from . import views

app_name = 'workout_hub_app'
urlpatterns = [
    # Workouts dashboard
    path('', views.workoutsHome, name='workouts'),
    # Create a workout dashboard
    path('create_workout/', views.create_workout, name='create_workout'),
    # view workouts
    path('workouts_dashboard/', views.workouts_dashboard, name='workouts_dashboard')
]
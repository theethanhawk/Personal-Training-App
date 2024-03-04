"""Defines URL patterns for pt_programs_app"""

from django.urls import path
from . import views

app_name = 'pt_programs_app'
urlpatterns = [
    # Metrics dashboard
    path('', views.programsHome, name='programs'),
    path('create_program/', views.createProgram, name='create_program'),
]
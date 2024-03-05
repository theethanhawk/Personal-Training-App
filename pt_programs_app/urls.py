"""Defines URL patterns for pt_programs_app"""

from django.urls import path
from . import views

app_name = 'pt_programs_app'
urlpatterns = [
    # Metrics dashboard
    path('', views.programsHome, name='programs'),
    path('create_program/', views.createProgram, name='create_program'),
    path('program/<int:pk>/', views.program_details, name='program_details'),
    path('build_program_weeks/', views.build_program_weeks, name='build_program_weeks'),
    #path('display_full_program/', views.display_program, name="display_program"),
]
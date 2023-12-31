"""Defines URL patterns for dashboard_app"""

from django.urls import path
from . import views

app_name = 'dashboard_app'
urlpatterns = [
    # Main dashboard
    path('', views.dashboard, name='dashboard')
]
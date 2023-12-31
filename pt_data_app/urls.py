"""Defines URL patterns for pt_data_app"""

from django.urls import path
from . import views

app_name = 'pt_data_app'
urlpatterns = [
    # Metrics dashboard
    path('', views.dataHome, name='data')
]
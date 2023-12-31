"""Defines URL patterns for health_metrics_app"""

from django.urls import path
from . import views

app_name = 'health_metrics_app'
urlpatterns = [
    # Metrics dashboard
    path('', views.metricsHome, name='metrics'),
    # Page for inputing health metrics
    path('add_health_metrics/', views.add_health_metrics, name='add_health_metrics_dashboard'),
    # Dashboard for viewing health data
    path('health_metrics_dashboard/', views.health_metrics_dashboard, name='health_metrics_dashboard'),
]
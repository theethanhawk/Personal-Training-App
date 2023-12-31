"""
URL configuration for personal_trainer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# ----------------------------------------------------------------
# Connects the urls from project apps to the personal_trainer urls
# ----------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard_app.urls')),
    path('goals/', include('goals_app.urls')),
    path('metrics/', include('health_metrics_app.urls')),
    path('data/', include('pt_data_app.urls')),
    path('programs/', include('pt_programs_app.urls')),
    path('workouts/', include('workout_hub_app.urls'))
]

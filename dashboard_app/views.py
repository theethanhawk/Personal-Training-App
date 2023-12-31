from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard_app/dashboard.html')

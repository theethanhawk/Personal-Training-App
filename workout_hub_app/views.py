from django.shortcuts import render

# Create your views here.

def workoutsHome(request):
    return render(request, 'workout_hub_app/workout_hub.html')
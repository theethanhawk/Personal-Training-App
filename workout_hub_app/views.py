from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from .models import Workout
from .forms import WorkoutForm

def workoutsHome(request):
    return render(request, 'workout_hub_app/workout_hub.html')

def create_workout(request):

    if request.method == 'POST':
        if 'workout_submit' in request.POST:
            workout_form = WorkoutForm(request.POST)
            if workout_form.is_valid():
                workout_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': workout_form.errors})
    
    else:
        workout_form = WorkoutForm()

    return render(request, 'workout_hub_app/create_workout.html', {
        'workout_form': workout_form
    })


def workouts_dashboard(request):
    workout_data = Workout.objects.all()

    return render(request, 'workout_hub_app/workouts_dashboard.html', {
        'workout_data': workout_data,
    })
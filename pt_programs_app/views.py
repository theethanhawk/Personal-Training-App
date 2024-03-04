from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import TrainingProgramForm

from .models import TrainingProgram, ActivityType

# Create your views here.

def programsHome(request):
    return render(request, 'pt_programs_app/pt_programs.html')


@login_required
def createProgram(request):
    """Renders the program form"""
    if request.method != 'POST':
        form = TrainingProgramForm()
    else:
        form = TrainingProgramForm(data=request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.owner = request.user
            program.save()

            activities = form.cleaned_data.get('activities')
            if activities:
                activities = [title.strip() for title in activities.split(',')]
                for a in activities:
                    activity_type, created = ActivityType.objects.get_or_create(title=a)
                    program.activity.add(activity_type)

            return redirect('pt_programs_app:programs')
    
    context = {
        'form': form,
    }
    return render(request, 'pt_programs_app/create_program.html', context)

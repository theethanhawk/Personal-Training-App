from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import TrainingProgramForm, TrainingWeekForm

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

            return redirect('pt_programs_app:program_details', pk=program.pk)
    
    context = {
        'form': form,
    }
    return render(request, 'pt_programs_app/create_program.html', context)


@login_required
def program_details(request, pk):
    """Renders program form data with button to continue building program"""
    program = get_object_or_404(TrainingProgram, pk=pk)
    return render(request, 'pt_programs_app/program_details.html', {'program': program})


@login_required
def build_program_weeks(request, pk):
    """Renders TrainingWeek forms for # of weeks in program_duration"""
    program = get_object_or_404(TrainingProgram, pk=pk)
    weeks = program.program_duration
    
    if request.method != 'POST':
        # Create a list of TrainingWeekForm instances based on the number of weeks in the program.
        forms = [TrainingWeekForm(prefix=str(i)) for i in range(weeks)]
        forms = [TrainingWeekForm(prefix=str(i), initial={'week_number': i + 1}) for i in range(weeks)]

        context = {
            'program': program,
            'forms': forms,
        }

        return render(request, 'pt_programs_app/build_program_weeks.html', context)

    else:
        # Create a list to store form instances with cleaned data.
        form_instances = []

        # Loop through each week's form in the request data.
        for i in range(weeks):
            form = TrainingWeekForm(request.POST, prefix=str(i), initial={'week_number': i + 1})
            
            if form.is_valid():
                # If the form is valid, save it to the list of form instances.
                week_instance = form.save(commit=False)
                week_instance.program = program  # Associate the week with the correct program
                week_instance.calculate_week_start_date()  # Calculate week_start_date
                week_instance.save()
                form_instances.append(week_instance)

        return redirect('pt_programs_app:program_details', pk=program.pk)
from django.shortcuts import render
from django.http import JsonResponse

from .models import (
    LongTermGoal, Goal, ActionObjective
)

from .forms import (
    LongTermGoalForm, GoalForm, ActionObjectiveForm
)


# Create your views here.

def goalsHome(request):
    return render(request, 'goals_app/goals.html')


def add_Goals(request):
    if request.method == 'POST':
        if 'longtermgoal_submit' in request.POST:
            longtermgoal_form = LongTermGoalForm(request.POST)
            if longtermgoal_form.is_valid():
                longtermgoal_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': longtermgoal_form.errors})
            
        elif 'goal_submit' in request.POST:
            goal_form = GoalForm(request.POST)
            if goal_form.is_valid():
                goal_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': goal_form.errors})
        
        elif 'actionobjective_submit' in request.POST:
            actionObjective_form = ActionObjectiveForm(request.POST)
            if actionObjective_form.is_valid():
                actionObjective_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': actionObjective_form.errors})

    else:
        longtermgoal_form = LongTermGoalForm()
        goal_form = GoalForm()
        actionObjective_form = ActionObjectiveForm()

    return render(request, 'goals_app/add_goals.html', {
        'longtermgoal_form': longtermgoal_form,
        'goal_form': goal_form,
        'actionObjective_form': actionObjective_form
    })


def display_Goals(request):
    LongTermGoal_data = LongTermGoal.objects.all().order_by('-created_at')
    Goal_data = Goal.objects.all().order_by('-created_at')
    actionObjective_data = ActionObjective.objects.all().order_by('-created_at')

    return render(request, 'goals_app/goals_display_dashboard.html', {
        'longTermGoal_data': LongTermGoal_data,
        'goal_data': Goal_data,
        'actionObjective_data': actionObjective_data
    })
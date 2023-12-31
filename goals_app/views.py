from django.shortcuts import render

# Create your views here.

def goalsHome(request):
    return render(request, 'goals_app/goals.html')

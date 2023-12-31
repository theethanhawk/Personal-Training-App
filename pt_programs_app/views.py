from django.shortcuts import render

# Create your views here.

def programsHome(request):
    return render(request, 'pt_programs_app/pt_programs.html')
from django.shortcuts import render

# Create your views here.

def dataHome(request):
    return render(request, 'pt_data_app/pt_data.html')
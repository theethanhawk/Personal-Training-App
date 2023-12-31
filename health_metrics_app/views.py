from django.shortcuts import render
from django.http import JsonResponse

from .models import (
    MorningHeartRate, HoursSlept, SleepQuality, ColdExposure, 
    ScreenTime, DietQuality, MobilityWork
)

from .forms import (
    MorningHeartRateForm, HoursSleptForm, SleepQualityForm, ColdExposureForm,
    ScreenTimeForm, DietQualityForm, MobilityWorkForm
)
# Create your views here.

def metricsHome(request):
    return render(request, 'health_metrics_app/metrics.html')

# This view allows me to add data for any of my health metrics
def add_health_metrics(request):
    if request.method == 'POST':
        # Check which form is being submitted
        if 'sleep_submit' in request.POST:  # Add a name attribute to the sleep form submit button
            sleep_form = SleepQualityForm(request.POST)
            if sleep_form.is_valid():
                sleep_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': sleep_form.errors})

        elif 'cold_submit' in request.POST:  # Add a name attribute to the cold form submit button
            cold_form = ColdExposureForm(request.POST)
            if cold_form.is_valid():
                cold_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': cold_form.errors})
            
        elif 'screen_submit' in request.POST:
            screen_form = ScreenTimeForm(request.POST)
            if screen_form.is_valid():
                screen_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': screen_form.errors})
            
        elif 'diet_submit' in request.POST:
            diet_form = DietQualityForm(request.POST)
            if diet_form.is_valid():
                diet_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': diet_form.errors})
            
        elif 'mobility_submit' in request.POST:
            mobility_form = MobilityWorkForm(request.POST)
            if mobility_form.is_valid():
                mobility_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': mobility_form.errors})
            
        elif 'heartrate_submit' in request.POST:
            heartrate_form = MorningHeartRateForm(request.POST)
            if heartrate_form.is_valid():
                heartrate_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': heartrate_form.errors})
            
        elif 'hoursslept_submit' in request.POST:
            hoursslept_form = HoursSleptForm(request.POST)
            if hoursslept_form.is_valid():
                hoursslept_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': hoursslept_form.errors})

    else:
        hoursslept_form = HoursSleptForm()
        morning_heartrate_form = MorningHeartRateForm()
        sleep_form = SleepQualityForm()
        cold_form = ColdExposureForm()
        screen_form = ScreenTimeForm()
        diet_form = DietQualityForm()
        mobility_form = MobilityWorkForm()

    return render(request, 'health_metrics_app/add_health_metrics_dashboard.html', {
        'hoursslept_form': hoursslept_form,
        'morning_heartrate_form': morning_heartrate_form,
        'sleep_form': sleep_form, 
        'cold_form': cold_form,
        'screen_form': screen_form,
        'diet_form': diet_form,
        'mobility_form': mobility_form,
    })


# Dashboard for displaying all data for health metrics
def health_metrics_dashboard(request):
    morning_heart_rate_data = MorningHeartRate.objects.all().order_by('-date')
    sleep_hours_data = HoursSlept.objects.all().order_by('-date')
    sleep_qualities = SleepQuality.objects.all().order_by('-date')
    cold_exposures = ColdExposure.objects.all().order_by('-date')
    screentime_data = ScreenTime.objects.all().order_by('-date')
    diet_quality_data = DietQuality.objects.all().order_by('-date')
    mobility_data = MobilityWork.objects.all().order_by('-date')
    return render(request, 'health_metrics_app/health_metrics_dashboard.html', {
        'morning_heart_rate_data': morning_heart_rate_data,
        'sleep_hours_data': sleep_hours_data,
        'screentime_data': screentime_data,
        'diet_quality_data': diet_quality_data,
        'mobility_data': mobility_data,
        'sleep_qualities': sleep_qualities,
        'cold_exposures': cold_exposures,
    })

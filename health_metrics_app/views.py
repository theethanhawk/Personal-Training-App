from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from .models import (
    MorningHeartRate, HoursSlept, SleepQuality, ColdExposure, 
    ScreenTime, DietQuality, MobilityWork, MorningWeight, MorningEnergy,
    DailyExercise, DayEnergy, FocusLevel,
    FreshAirExposure, SocialConnection
)

from .forms import (
    MorningHeartRateForm, HoursSleptForm, SleepQualityForm, ColdExposureForm,
    ScreenTimeForm, DietQualityForm, MobilityWorkForm, MorningWeightForm,
    MorningEnergyForm, DailyExerciseForm, DayEnergyForm, FocusLevelForm, 
    FreshAirExposureForm, SocialConnectionForm
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
            
        elif 'socialconnection_submit' in request.POST:  # Add a name attribute to the cold form submit button
            socialconnection_form = SocialConnectionForm(request.POST)
            if socialconnection_form.is_valid():
                socialconnection_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': socialconnection_form.errors})
            
        elif 'freshair_submit' in request.POST:  # Add a name attribute to the cold form submit button
            freshair_form = FreshAirExposureForm(request.POST)
            if freshair_form.is_valid():
                freshair_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': freshair_form.errors})
            
        elif 'focuslevel_submit' in request.POST:  # Add a name attribute to the cold form submit button
            focuslevel_form = FocusLevelForm(request.POST)
            if focuslevel_form.is_valid():
                focuslevel_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': focuslevel_form.errors})
            
        elif 'dayenergy_submit' in request.POST:  # Add a name attribute to the cold form submit button
            dayenergy_form = DayEnergyForm(request.POST)
            if dayenergy_form.is_valid():
                dayenergy_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': dayenergy_form.errors})
            
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
            
        elif 'morningweight_submit' in request.POST:
            morningweight_form = MorningWeightForm(request.POST)
            if morningweight_form.is_valid():
                morningweight_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': morningweight_form.errors})
            
        elif 'morningenergy_submit' in request.POST:
            morningenergy_form = MorningEnergyForm(request.POST)
            if morningenergy_form.is_valid():
                morningenergy_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': morningenergy_form.errors})
            
        elif 'dailyexercise_submit' in request.POST:
            dailyexercise_form = DailyExerciseForm(request.POST)
            if dailyexercise_form.is_valid():
                dailyexercise_form.save()
                return JsonResponse({'success': True})  # Respond with JSON for AJAX
            else:
                return JsonResponse({'success': False, 'errors': dailyexercise_form.errors})

    else:
        hoursslept_form = HoursSleptForm()
        morning_heartrate_form = MorningHeartRateForm()
        sleep_form = SleepQualityForm()
        cold_form = ColdExposureForm()
        screen_form = ScreenTimeForm()
        diet_form = DietQualityForm()
        mobility_form = MobilityWorkForm()
        morningweight_form = MorningWeightForm()
        morningenergy_form = MorningEnergyForm()
        dailyexercise_form = DailyExerciseForm()
        dayenergy_form = DayEnergyForm()
        focuslevel_form = FocusLevelForm()
        freshair_form = FreshAirExposureForm()
        socialconnection_form = SocialConnectionForm()


    return render(request, 'health_metrics_app/add_health_metrics_dashboard.html', {
        'hoursslept_form': hoursslept_form,
        'morning_heartrate_form': morning_heartrate_form,
        'sleep_form': sleep_form, 
        'cold_form': cold_form,
        'screen_form': screen_form,
        'diet_form': diet_form,
        'mobility_form': mobility_form,
        'morningweight_form': morningweight_form,
        'morningenergy_form': morningenergy_form,
        'dailyexercise_form': dailyexercise_form,
        'dayenergy_form': dayenergy_form,
        'focuslevel_form': focuslevel_form,
        'freshair_form': freshair_form,
        'socialconnection_form': socialconnection_form,
    })


# Dashboard for displaying all data for health metrics
def health_metrics_dashboard(request):
    current_date = timezone.now().date()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day 

    morning_heart_rate_data = MorningHeartRate.objects.all().order_by('-date')
    sleep_hours_data = HoursSlept.objects.all().order_by('-date')
    sleep_qualities = SleepQuality.objects.all().order_by('-date')
    cold_exposures = ColdExposure.objects.all().order_by('-date')
    screentime_data = ScreenTime.objects.all().order_by('-date')
    diet_quality_data = DietQuality.objects.all().order_by('-date')
    mobility_data = MobilityWork.objects.all().order_by('-date')
    morningweight_data = MorningWeight.objects.all().order_by('-date')
    morningenergy_data = MorningEnergy.objects.all().order_by('-date')
    dailyexercise_data = DailyExercise.objects.all().order_by('-date')
    dayenergy_data = DayEnergy.objects.all().order_by('-date')
    focuslevel_data = FocusLevel.objects.all().order_by('-date')
    freshair_data = FreshAirExposure.objects.all().order_by('-date')
    socialconnection_data = SocialConnection.objects.all().order_by('-date')

    daily_exercise_count = DailyExercise.objects.filter(
        date__year=current_year, 
        date__month=current_month, 
        date__day__lte=current_day,  # Less than or equal to current day
        completed=True
    ).count()

    daily_exercise_percentage = (daily_exercise_count / current_day) * 100

    return render(request, 'health_metrics_app/health_metrics_dashboard.html', {
        'morning_heart_rate_data': morning_heart_rate_data,
        'sleep_hours_data': sleep_hours_data,
        'screentime_data': screentime_data,
        'diet_quality_data': diet_quality_data,
        'mobility_data': mobility_data,
        'sleep_qualities': sleep_qualities,
        'cold_exposures': cold_exposures,
        'morningweight_data': morningweight_data,
        'morningenergy_data': morningenergy_data,
        'dailyexercise_data': dailyexercise_data,
        'dayenergy_data': dayenergy_data,
        'focuslevel_data': focuslevel_data,
        'freshair_data': freshair_data,
        'socialconnection_data': socialconnection_data,
        'daily_exercise_percentage': daily_exercise_percentage,
    })

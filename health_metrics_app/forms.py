from django import forms

from .models import (
    MorningHeartRate, HoursSlept, SleepQuality, ColdExposure, 
    ScreenTime, DietQuality, MobilityWork, MorningWeight, MorningEnergy,
    DailyExercise, DayEnergy, FocusLevel,
    FreshAirExposure, SocialConnection
)


class MorningHeartRateForm(forms.ModelForm):
    class Meta:
        model = MorningHeartRate
        fields = ['rate', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_morning_heartrate_date'}),
            'rate': forms.NumberInput(attrs={'id': 'id_morning_heart_rate'}),
        }


class MorningWeightForm(forms.ModelForm):
    class Meta:
        model = MorningWeight
        fields = ['weight', 'date']
        widgets = {
            'weight': forms.NumberInput(attrs={'id': 'id_morning_weight'}),
            'date': forms.DateInput(attrs={'id': 'id_morning_weight_date'}),
        }

class HoursSleptForm(forms.ModelForm):
    class Meta:
        model = HoursSlept
        fields = ['hours', 'date']
        widgets = {
            'hours': forms.NumberInput(attrs={'id': 'id_hours_slept'}),
            'date': forms.DateInput(attrs={'id': 'id_hours_slept_date'}),
        }


class SleepQualityForm(forms.ModelForm):
    class Meta:
        model = SleepQuality
        fields = ['date', 'quality']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_sleep_date'}),
            'quality': forms.Select(attrs={'id': 'id_sleep_quality'}),
        }


class MorningEnergyForm(forms.ModelForm):
    class Meta:
        model = MorningEnergy
        fields = ['date', 'level']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_morning_energy_date'}),
            'level': forms.Select(attrs={'id': 'id_morning_energy_level'}),
        }


class DailyExerciseForm(forms.ModelForm):
    class Meta:
        model = DailyExercise
        fields = ['date', 'completed']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_daily_exercise_date'}),
            'completed': forms.CheckboxInput(attrs={'id': 'id_daily_exercise_completed'}),
        }


class DietQualityForm(forms.ModelForm):
    class Meta:
        model = DietQuality
        fields = ['date', 'quality']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_diet_date'}),
            'quality': forms.Select(attrs={'id': 'id_diet_quality'}),
        }


class MobilityWorkForm(forms.ModelForm):
    class Meta:
        model = MobilityWork
        fields = ['date', 'completed']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_mobility_date'}),
            'completed': forms.CheckboxInput(attrs={'id': 'id_mobility_completed'}),
        }


class DayEnergyForm(forms.ModelForm):
    class Meta:
        model = DayEnergy
        fields = ['date', 'level']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_day_energy_date'}),
            'level': forms.Select(attrs={'id': 'id_day_energy_level'}),
        }


class FocusLevelForm(forms.ModelForm):
    class Meta:
        model = FocusLevel
        fields = ['date', 'level']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_focus_level_date'}),
            'level': forms.Select(attrs={'id': 'id_focus_level'}),
        }


class ScreenTimeForm(forms.ModelForm):
    class Meta:
        model = ScreenTime
        fields = ['time', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_screentime_date'}),
            'time': forms.NumberInput(attrs={'id': 'id_screen_time'}),
        }


class ColdExposureForm(forms.ModelForm):
    class Meta:
        model = ColdExposure
        fields = ['date', 'exposed']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_cold_date'}),
            'exposed': forms.CheckboxInput(attrs={'id': 'id_cold_exposed'}),
        }


class FreshAirExposureForm(forms.ModelForm):
    class Meta:
        model = FreshAirExposure
        fields = ['date', 'exposure']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_fresh_air_date'}),
            'exposure': forms.CheckboxInput(attrs={'id': 'id_freshair_exposure'}),
        }


class SocialConnectionForm(forms.ModelForm):
    class Meta:
        model = SocialConnection
        fields = ['date', 'connection']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_social_connection_date'}),
            'connection': forms.CheckboxInput(attrs={'id': 'id_social_connection'}),
        }
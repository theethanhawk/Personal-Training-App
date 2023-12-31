from django import forms

from .models import (
    MorningHeartRate, HoursSlept, SleepQuality, ColdExposure, 
    ScreenTime, DietQuality, MobilityWork
)


class MorningHeartRateForm(forms.ModelForm):
    class Meta:
        model = MorningHeartRate
        fields = ['rate', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_morning_heartrate_date'}),
            'rate': forms.NumberInput(attrs={'id': 'id_morning_heart_rate'}),
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


class ColdExposureForm(forms.ModelForm):
    class Meta:
        model = ColdExposure
        fields = ['date', 'exposed']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_cold_date'}),
            'exposed': forms.CheckboxInput(attrs={'id': 'id_cold_exposed'}),
        }


class ScreenTimeForm(forms.ModelForm):
    class Meta:
        model = ScreenTime
        fields = ['time', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'id': 'id_screentime_date'}),
            'time': forms.NumberInput(attrs={'id': 'id_screen_time'}),
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
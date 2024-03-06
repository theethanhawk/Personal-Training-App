"""File to handle form structures"""

from django import forms

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column

from .models import (
    ActivityType, TrainingWeek, TrainingProgram, TrainingEvent  #TrainingDay
)

class TrainingProgramForm(forms.ModelForm):
    activities = forms.CharField(
        max_length=50,
        required=False,
        help_text="Select training activities that will be part of this program."
    )

    class Meta:
        model = TrainingProgram
        fields = ['program_name', 'program_duration', 'start_date', 'program_details']
        widgets = {
            'program_name': forms.TextInput(attrs={'id': 'id_program_name'}),
            'program_duration': forms.NumberInput(attrs={'id': 'id_program_duration'}),
            'start_date': forms.DateInput(attrs={'id': 'id_start_date'}),
            'program_details': forms.TextInput(attrs={'id': 'id_program_details'})
        }


class TrainingWeekForm(forms.ModelForm):
    week_number = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = TrainingWeek
        fields = ['week_title', 'week_description']


class TrainingEventForm(forms.ModelForm):
    event_activity = forms.CharField(
        max_length=50,
        required=False,
        help_text="Select training activities that will be part of this training block."
    )

    class Meta:
        model = TrainingEvent
        fields = ['day_of_week', 'event_block']
        widgets = {
            'day_of_week': forms.NumberInput(attrs={'id': 'id_day_of_week'}),
            'event_block': forms.Select(attrs={'id': 'id_event_block'})
        }


# class TrainingDayForm(forms.ModelForm):
#     class Meta:
#         model = TrainingDay
#         fields = ['day_of_week']
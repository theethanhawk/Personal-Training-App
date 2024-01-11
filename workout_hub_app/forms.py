from django import forms

from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'date', 'description', 'pre_note', 'post_note']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'id_workout_title'}),
            'date': forms.DateInput(attrs={'id':'id_workout_date'}),
            'description': forms.Textarea(attrs={'id': 'id_workout_description'}),
            'pre_note': forms.Textarea(attrs={'id': 'id_workout_pre_note'}),
            'post_note': forms.Textarea(attrs={'id': 'id_workout_post_note'}),
        }
from django import forms

from .models import (
    LongTermGoal, Goal, ActionObjective
)

class LongTermGoalForm(forms.ModelForm):
    class Meta:
        model = LongTermGoal
        fields = ['title', 'description', 'created_at', 'timeframe']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'id_longterm_goal_title'}),
            'description': forms.TextInput(attrs={'id': 'id_longTermGoal_description'}),
            'created_at': forms.DateInput(attrs={'id': 'id_longtermgoal_created_at'}),
            'timeframe': forms.NumberInput(attrs={'id': 'id_longTermGoal_timeframe'}),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            'title', 'definition', 'actionObjectiveAbstract', 'created_at', 'measuresAbstract',
            'is_completed',
            ]
        widgets = {
            'title': forms.TextInput(attrs={'id': 'id_goal_title'}),
            'definition': forms.TextInput(attrs={'id': 'id_goal_definition'}),
            'actionObjectiveAbstract': forms.TextInput(attrs={'id': 'id_goal_actionObjectiveAbstract'}),
            'created_at': forms.DateInput(attrs={'id': 'id_goal_created_at'}),
            'measuresAbstract': forms.TextInput(attrs={'id': 'id_goal_measuresAbstract'}),
            'is_completed': forms.CheckboxInput(attrs={'id': 'id_goal_is_completed'}),
        }

class ActionObjectiveForm(forms.ModelForm):
    class Meta:
        model = ActionObjective
        fields = ['goal', 'actionDefinition', 'hours_per_week', 'hours_per_day', 'created_at', 'is_completed']
        widgets = {
            'goal': forms.Select(attrs={'id': 'id_actionObjective_goal'}),
            'actionDefinition': forms.TextInput(attrs={'id': 'id_actionObjective_actionDefinition'}),
            'hours_per_week': forms.NumberInput(attrs={'id': 'id_actionObjective_hours_per_week'}),
            'hours_per_day': forms.NumberInput(attrs={'id': 'id_actionObjective_hours_per_day'}),
            'created_at': forms.DateInput(attrs={'id': 'id_actionObjective_created_at'}),
            'is_completed': forms.CheckboxInput(attrs={'id': 'id_actionObjective_is_completed'}),
        }


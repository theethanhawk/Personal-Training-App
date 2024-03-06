"""This file handles models for my training programs"""
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

from workout_hub_app.models import Workout

# Create your models here.

# This model will be used for activity data tracking so it needs to be pretty simple
#  practically functions as a tag for the type of activity focused on in a given workout
class ActivityType(models.Model):
    """Type name for different training activities"""
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """Returns string representation of tag"""
        return self.title


class TrainingProgram(models.Model):
    """Names and stores training program information"""
    program_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    program_duration = models.PositiveIntegerField() # Duration in weeks
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    program_details = models.TextField(blank=True)
    program_notes = models.TextField(blank=True)
    activity = models.ManyToManyField(ActivityType, blank=True)

    def clean(self):
        # Ensure program_duration is valid.
        if self.program_duration < 1:
            raise ValidationError({'program_duration': 'Duration must be at least 1 week.'})
        # Ensure start_date is not in the past.
        if self.start_date < timezone.now().date():
            raise ValidationError({'start_date': 'Start date cannot be in the past.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate model before saving
        # Calculate end_date based on start_date and program_duration
        if self.start_date and self.program_duration is not None:
            self.end_date = self.start_date + timedelta(days=self.program_duration * 7 - 1)
        super(TrainingProgram, self).save(*args, **kwargs)

    def __str__(self):
        """Returns the program name"""
        return self.program_name


class TrainingWeek(models.Model):
    """Representation of a full week of training"""
    program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, related_name='training_weeks', null=True)
    week_title = models.CharField(max_length=100)
    week_description = models.CharField(max_length=200)
    week_start_date = models.DateField() #Determined in the views
    week_number = models.PositiveIntegerField(null=True) 

    def calculate_week_start_date(self):
        self.week_number = self.program.program_duration
        week_count = 0
    
        if self.program and self.program.start_date:
            while week_count < self.week_number:
                print(week_count)
                days_offset = week_count * 7
                self.week_start_date = self.program.start_date + timedelta(days=days_offset)
                print(days_offset)
                week_count += 1


    # def calculate_week_start_date(self):
    #     if self.program and self.program.start_date:
    #         self.week_number = self.program.program_duration
    #         print(self.week_number)
    #         # Calculates for Week 1 set to day 0 (start_date), week 2 to day 7, etc.
    #         days_offset = (self.week_number - 1) * 7
    #         self.week_start_date = self.program.start_date + timedelta(days=days_offset)
        

    def __str__(self):
        """Returns the title of the weeks training"""
        return self.week_title


class TrainingEvent(models.Model):
    """Representation details of one event in a days training"""
    event_activity = models.ManyToManyField(ActivityType, blank=True)
    DAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]
    day_of_week = models.IntegerField(choices=DAY_CHOICES, default=0)
    MORNING = 'morning'
    EVENING = 'evening'
    TRAINING_BLOCK_CHOICES = [
        (MORNING, 'Morning training'),
        (EVENING, 'Evening training'),
    ]
    event_block = models.CharField(max_length=7, choices=TRAINING_BLOCK_CHOICES)
    session_workout = models.ForeignKey(
        Workout, related_name='training_days', on_delete=models.CASCADE,
        null=True, blank=True,
        )


    def __str__(self):
        """Returns which event block is being specified"""
        return self.event_block


# class TrainingDay(models.Model):
#     """Holds TrainingEvent's withi a TrainingDay in a given TrainingWeek"""
#     session = models.ManyToManyField(TrainingEvent, blank=True)
#     training_date = models.DateField()

#     training_week = models.ForeignKey(TrainingWeek, on_delete=models.CASCADE)
#     session_workout = models.ForeignKey(
#         Workout, related_name='training_days', on_delete=models.CASCADE,
#         null=True, blank=True,
#         )

#     def __str__(self):
#         """Returns a string representation of the date"""
#         return f"{self.get_day_of_week_display()} - {self.training_date}"

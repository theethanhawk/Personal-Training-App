from django.db import models
from pt_programs_app.models import TrainingEvent

# Create your models here.

#-----------------------
# Workout related models
#-----------------------

# Given the nature of workouts and training events, a ForeignKey in the Workout model 
#  pointing back to TrainingEvent might make sense.
class Workout(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    pre_note = models.TextField()
    post_note = models.TextField()
    training_event = models.ForeignKey(TrainingEvent, on_delete=models.CASCADE, related_name='workouts', null=True, blank=True)

    class Meta:
        unique_together = ('title', 'date')

    def __str__(self):
        return f"{self.title} on {self.date}"
    
    
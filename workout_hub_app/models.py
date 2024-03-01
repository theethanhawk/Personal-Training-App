from django.db import models

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

    class Meta:
        unique_together = ('title', 'date')

    def __str__(self):
        return f"{self.title} on {self.date}"

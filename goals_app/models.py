from django.db import models
from django.utils import timezone

# Create your models here.

#-------------------------
# Goal related models here
#-------------------------


class LongTermGoal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timeframe = models.PositiveIntegerField()# measure between 3-5 years
    created_at = models.DateField()

    def __str__(self):
        return self.title


class Goal(models.Model):
    title = models.CharField(max_length=200)
    longtermGoal = models.ManyToManyField(LongTermGoal)
    definition = models.TextField()
    actionObjectiveAbstract = models.TextField()
    measuresAbstract = models.TextField()
    created_at = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class ActionObjective(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    actionDefinition = models.CharField(max_length=400)
    hours_per_week = models.PositiveIntegerField()  #time frame for hours
    hours_per_day = models.PositiveIntegerField()  #time frame for hours
    created_at = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    # MON = 'monday'
    # TUE = 'tuesday'
    # WED = 'wednesday'
    # THU = 'thursday'
    # FRI = 'friday'
    # SAT = 'saturday'
    # SUN = 'sunday'
    # DAY_OF_WEEK_CHOICES = [
    #     (MON, 'Monday'),
    #     (TUE, 'Tuesday'),
    #     (WED, 'Wednesday'),
    #     (THU, 'Thursday'),
    #     (FRI, 'Friday'),
    #     (SAT, 'Saturday'),
    #     (SUN, 'Sunday'),
    # ]
    # days_per_week = models.CharField(max_length=9, choices=DAY_OF_WEEK_CHOICES)

    def __str__(self):
        return f"{self.goal} requires {self.actionDefinition}"
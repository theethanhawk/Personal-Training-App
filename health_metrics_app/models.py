from django.db import models

# Create your models here.

# ----------------------------
# Morning health metric models
# ----------------------------

class MorningHeartRate(models.Model):
    rate = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Morning Heart Rate: {self.rate} at {self.date.strftime('%Y-%m-%d')}"
    

class HoursSlept(models.Model):
    hours = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Hours slept {self.hours} on {self.date.strftime('%Y-%m-%d')}"


class SleepQuality(models.Model):
    POOR = 'poor'
    DECENT = 'decent'
    GOOD = 'good'
    GREAT = 'great'
    SLEEP_QUALITY_CHOICES = [
        (POOR, 'Poor Sleep'),
        (DECENT, 'Decent Sleep'),
        (GOOD, 'Good Sleep'),
        (GREAT, 'Great Sleep'),
    ]

    date = models.DateField()
    quality = models.CharField(max_length=6, choices=SLEEP_QUALITY_CHOICES)

    def __str__(self):
        return f"{self.date}: {self.get_quality_display()}"
    

class ColdExposure(models.Model):
    date = models.DateField()
    exposed = models.BooleanField()

    def __str__(self):
        return f"{self.date}: {'Yes' if self.exposed else 'No'}"
    

# -------------------------------
# End of day health metric models
# -------------------------------
    

class ScreenTime(models.Model):
    time = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.time} screentime on {self.date.strftime('%Y-%m-%d')}"
    

class DietQuality(models.Model):
    POOR = 'poor'
    DECENT = 'decent'
    GOOD = 'good'
    GREAT = 'great'
    DIET_QUALITY_CHOICES = [
        (POOR, 'Poor Diet'),
        (DECENT, 'Decent Diet'),
        (GOOD, 'Good Diet'),
        (GREAT, 'Great Diet'),
    ]

    date = models.DateField()
    quality = models.CharField(max_length=6, choices=DIET_QUALITY_CHOICES)

    def __str__(self):
        return f"{self.date}: {self.get_quality_display()}"
    

class MobilityWork(models.Model):
    date = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return f"{self.date}: {'Yes' if self.completed else 'No'}"
    

"""Data sets to add"""
# completed daily mobility and stretching - Boolean
# did I have any healthy sex - Choices
# did I get outside, particularly in the beginning of the day - Boolean
# drug consumption? - Choices
# did I exercise that day - Boolean
# quality of exercise - Choices
# was my diet in a deficit or excess
# social connection - choices
# energy level 1-5 - choices
# mood 1-5 - choices
# focus/productivity 1-5 - choices
# daily vitamins - boolean
# cold exposure - boolean
# other medications - choices
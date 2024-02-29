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


class MorningWeight(models.Model):
    weight = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Weight {self.weight}lbs on {self.date}"
    

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
    

class MorningEnergy(models.Model):
    LOW = 'low'
    AVERAGE = 'average'
    GOOD = 'good'
    HIGH = 'high'
    ENERGY_LEVEL_CHOICES = [
        (LOW, 'Low Energy'),
        (AVERAGE, 'Average Energy'),
        (GOOD, 'Good Energy'),
        (HIGH, 'High Energy'),
    ]

    date = models.DateField()
    level = models.CharField(max_length=7, choices=ENERGY_LEVEL_CHOICES)

    def __str__(self):
        return f"{self.date}: {self.get_level_display()}"

# ------------------------
# Day health metric models
# ------------------------
    

class DailyExercise(models.Model):
    date = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return f"{self.date}: {'Yes' if self.completed else 'No'}"
    

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
    

class DayEnergy(models.Model):
    LOW = 'low'
    AVERAGE = 'average'
    GOOD = 'good'
    HIGH = 'high'
    ENERGY_LEVEL_CHOICES = [
        (LOW, 'Low Energy'),
        (AVERAGE, 'Average Energy'),
        (GOOD, 'Good Energy'),
        (HIGH, 'High Energy'),
    ]

    date = models.DateField()
    level = models.CharField(max_length=7, choices=ENERGY_LEVEL_CHOICES)

    def __str__(self):
        return f"{self.date}: {self.get_level_display()}"


class FocusLevel(models.Model):
    DISTRACTED = 'distracted'
    MIXED = 'mixed'
    FOCUSED = 'focused'
    FOCUS_LEVEL_CHOICES = [
        (DISTRACTED, 'Distracted Mind'),
        (MIXED, 'Mixed Mind'),
        (FOCUSED, 'Focused Mind'),
    ]

    date = models.DateField()
    level = models.CharField(max_length=10, choices=FOCUS_LEVEL_CHOICES)

    def __str__(self):
        return f"{self.date}: {self.get_level_display()}"   
    

#----------------------
# Mental Health Metrics
#----------------------

class ScreenTime(models.Model):
    time = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.time}hours of screentime on {self.date.strftime('%Y-%m-%d')}"
    
class ColdExposure(models.Model):
    date = models.DateField()
    exposed = models.BooleanField()

    def __str__(self):
        return f"{self.date}: {'Yes' if self.exposed else 'No'}"
    

class FreshAirExposure(models.Model):
    date = models.DateField()
    exposure = models.BooleanField()

    def __str__(self):
        return f"{self.date}: {'Yes' if self.exposure else 'No'}"
    

class SocialConnection(models.Model):
    date = models.DateField()
    connection = models.BooleanField()

    def __str__(self):
        return f"{self.date}: {'Yes' if self.connection else 'No'}"

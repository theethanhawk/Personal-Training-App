from django.contrib import admin

# Register your models here.

from .models import (
    MorningHeartRate, HoursSlept, SleepQuality, ColdExposure, 
    ScreenTime, DietQuality, MobilityWork, MorningWeight, MorningEnergy,
    DailyExercise, DayEnergy, FocusLevel,
    FreshAirExposure, SocialConnection
)

admin.site.register(MorningHeartRate)
admin.site.register(HoursSlept)
admin.site.register(SleepQuality)
admin.site.register(ColdExposure)
admin.site.register(ScreenTime)
admin.site.register(DietQuality)
admin.site.register(MobilityWork)
admin.site.register(MorningWeight)
admin.site.register(MorningEnergy)
admin.site.register(DailyExercise)
admin.site.register(DayEnergy)
admin.site.register(FocusLevel)
admin.site.register(FreshAirExposure)
admin.site.register(SocialConnection)

from django.contrib import admin

# Register your models here.

from .models import (
    MorningHeartRate, HoursSlept, SleepQuality, ColdExposure, 
    ScreenTime, DietQuality, MobilityWork
)

admin.site.register(MorningHeartRate)
admin.site.register(HoursSlept)
admin.site.register(SleepQuality)
admin.site.register(ColdExposure)
admin.site.register(ScreenTime)
admin.site.register(DietQuality)
admin.site.register(MobilityWork)

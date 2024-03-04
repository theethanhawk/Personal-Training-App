from django.contrib import admin

# Register your models here.

from .models import (
    ActivityType, TrainingWeek, TrainingProgram, TrainingEvent, # TrainingDay,
)

admin.site.register(ActivityType)
admin.site.register(TrainingWeek)
admin.site.register(TrainingProgram)
# admin.site.register(TrainingDay)
admin.site.register(TrainingEvent)
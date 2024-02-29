from django.contrib import admin

# Register your models here.

from .models import (
    ActivityType, TrainingWeek, TrainingProgram, TrainingDay, TrainingEvent
)

admin.site.register(ActivityType)
admin.site.register(TrainingWeek)
admin.site.register(TrainingProgram)
admin.site.register(TrainingDay)
admin.site.register(TrainingEvent)
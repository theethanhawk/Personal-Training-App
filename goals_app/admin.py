from django.contrib import admin

# Register your models here.

from .models import (
    LongTermGoal, Goal, ActionObjective
)

admin.site.register(LongTermGoal)
admin.site.register(Goal)
admin.site.register(ActionObjective)
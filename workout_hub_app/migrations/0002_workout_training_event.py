# Generated by Django 5.0 on 2024-02-29 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pt_programs_app', '0001_initial'),
        ('workout_hub_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='training_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='pt_programs_app.trainingevent'),
        ),
    ]

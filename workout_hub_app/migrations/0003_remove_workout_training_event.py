# Generated by Django 5.0 on 2024-03-01 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_hub_app', '0002_workout_training_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='training_event',
        ),
    ]

# Generated by Django 5.0 on 2024-01-11 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_metrics_app', '0002_dailyexercise_dayenergy_drugconsumption_focuslevel_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DrugConsumption',
        ),
    ]

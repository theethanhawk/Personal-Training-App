# Generated by Django 5.0 on 2023-12-31 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColdExposure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('exposed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DietQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quality', models.CharField(choices=[('poor', 'Poor Diet'), ('decent', 'Decent Diet'), ('good', 'Good Diet'), ('great', 'Great Diet')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='HoursSlept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MobilityWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('completed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MorningHeartRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ScreenTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SleepQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quality', models.CharField(choices=[('poor', 'Poor Sleep'), ('decent', 'Decent Sleep'), ('good', 'Good Sleep'), ('great', 'Great Sleep')], max_length=6)),
            ],
        ),
    ]
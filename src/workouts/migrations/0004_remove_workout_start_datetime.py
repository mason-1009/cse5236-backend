# Generated by Django 4.2.6 on 2023-11-23 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_remove_workout_duration_workout_duration_minutes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='start_datetime',
        ),
    ]

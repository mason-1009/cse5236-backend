# Generated by Django 4.2.6 on 2023-11-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_alter_workout_workout_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='duration',
        ),
        migrations.AddField(
            model_name='workout',
            name='duration_minutes',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

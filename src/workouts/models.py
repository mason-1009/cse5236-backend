from django.db import models

from backend.models import UUIDMixin, BaseMixin
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _gt


class Workout(UUIDMixin, BaseMixin):
    '''
    Represents a workout for a user; is linked via foreign key
    to a user.
    '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workouts'
    )

    class WorkoutChoices(models.TextChoices):
        WALKING = 'walking', _gt('Walking')
        RUNNING = 'running', _gt('Running')
        CYCLING = 'cycling', _gt('Cycling')
        SWIMMING = 'swimming', _gt('Swimming')
        HIKING = 'hiking', _gt('Hiking')
        WEIGHT_TRAINING = 'weight_training', _gt('Weight Training')
        ELIPTICAL = 'eliptical', _gt('Eliptical')
        OTHER = 'other', _gt('Other')

    workout_type = models.CharField(
        max_length=36,
        null=False,
        blank=False,
        choices=WorkoutChoices.choices,
        default=WorkoutChoices.OTHER
    )

    duration = models.DurationField(
        null=True,
        blank=False
    )

    distance_miles = models.PositiveIntegerField(
        null=True,
        blank=False
    )

    calories_burned = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    avg_heart_rate = models.PositiveIntegerField(
        null=True,
        blank=False
    )

    max_heart_rate = models.PositiveIntegerField(
        null=True,
        blank=False
    )

    start_datetime = models.DateTimeField(
        null=False,
        blank=False
    )

    # Override save to run a full_clean method
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

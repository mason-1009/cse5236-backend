from backend.models import BaseMixin, UUIDMixin
from django.db import models

from django.contrib.auth.models import User


class Food(models.Model):
    '''
    Represents a food.
    '''
    fdc_id = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        primary_key=True
    )

    data_type = models.CharField(
        max_length=64,
        null=False,
        blank=False
    )

    description = models.CharField(
        max_length=256,
        null=False,
        unique=False
    )


class NutrientType(models.Model):
    '''
    Represents a type of nutrient and its unit data (kcal, grams,
    carbs, etc.)
    '''
    nutrient_id = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        primary_key=True
    )

    name = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )

    unit_name = models.CharField(
        max_length=12,
        blank=False,
        null=False
    )


class FoodNutrient(models.Model):
    '''
    Represents nutrient information for a given food item.
    '''
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name='nutrients'
    )

    nutrient_type = models.ForeignKey(
        NutrientType,
        on_delete=models.CASCADE,
        related_name='nutrients'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=False,
        null=False
    )


class Meal(UUIDMixin, BaseMixin):
    '''
    Represents a recorded meal for a user.
    '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='meals'
    )

    calories = models.PositiveIntegerField(
        null=False,
        default=0
    )

    protein_grams = models.PositiveIntegerField(
        null=False,
        default=0
    )

    carbs_grams = models.PositiveIntegerField(
        null=False,
        default=0
    )

    fat_grams = models.PositiveIntegerField(
        null=False,
        default=0
    )

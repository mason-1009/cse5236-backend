from django.db import models


class FoodCategory(models.Model):
    '''
    Generic category of food type.
    '''
    category_id = models.IntegerField(
        null=False,
        blank=False,
        unique=True,
        primary_key=True
    )

    code = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        unique=True
    )

    name = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )


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

    category = models.ForeignKey(
        FoodCategory,
        null=True,
        on_delete=models.CASCADE,
        related_name='foods'
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

from django.db import models


class BaseMixin(models.Model):
    '''
    Base mixin for gracing other models with date created and modified.
    '''
    created = models.DateTimeField(
        auto_now_add=True,
        primary_key=False
    )

    updated = models.DateTimeField(
        auto_now=True,
        primary_key=False
    )

    class Meta:
        abstract = True

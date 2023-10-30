from django.db import models
from uuid import uuid4


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


class UUIDMixin(models.Model):
    '''
    Base mixin for providing inheriting models with a UUID as
    a primary key.
    '''
    uuid = models.UUIDField(
        blank=False,
        null=False,
        default=uuid4,
        primary_key=True
    )

    class Meta:
        abstract = True

from django.db import models


class BaseMixin(models.Model):
    '''
    Base mixin for gracing other models with date created and modified.
    '''
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

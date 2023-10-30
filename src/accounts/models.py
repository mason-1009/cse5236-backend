import uuid

from django.db import models
from backend.models import BaseMixin, UUIDMixin
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _gt


class UserAuthToken(BaseMixin):
    '''
    Represents an auth token for a user; generated for each login attempt.
    '''
    token_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=False
    )

    key = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        unique=False
    )



class UserInformation(BaseMixin):
    '''
    Model containing extra information about a user; linked to a Django User
    object via one-to-one foreign key.
    '''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    age = models.PositiveIntegerField(
        null=False
    )

    height_in_inches = models.PositiveIntegerField(
        null=False
    )

    class SexChoices(models.TextChoices):
        MALE = 'male', _gt('Male')
        FEMALE = 'female', _gt('Female')

    sex = models.CharField(
        max_length=36,
        choices=SexChoices.choices
    )

    starting_weight_pounds = models.PositiveIntegerField(
        blank=False,
        null=False
    )

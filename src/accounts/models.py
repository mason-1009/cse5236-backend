import uuid

from django.db import models
from backend.models import BaseMixin
from django.contrib.auth.models import User


class UserAuthToken(BaseMixin):
    '''
    Represents an auth token for a user; generated for each login attempt.
    '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=False
    )

    key = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
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

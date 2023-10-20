from uuid import UUID
from typing import Union

from accounts.models import UserAuthToken
from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: Union[UUID, str]):
        auth_token = UserAuthToken.objects.get(key=token)
        return auth_token.user

from uuid import UUID
from typing import Union

from accounts.models import UserAuthToken
from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: Union[UUID, str]):
        try:
            auth_token = UserAuthToken.objects.get(key=token)
        except Exception:
            # None-returns result in 401 unauthorized messages
            return None

        return auth_token.user

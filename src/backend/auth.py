from uuid import UUID
from typing import Union

from accounts.models import UserAuthToken
from ninja.security import APIKeyHeader


class APIKeyAuth(APIKeyHeader):
    param_name = 'X-API-Key'

    def authenticate(self, request, key: Union[UUID, str]):
        try:
            auth_token = UserAuthToken.objects.get(key=key)
        except Exception:
            # None-returns result in 401 unauthorized messages
            return None

        return auth_token.user

from ninja import Router
import logging

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from accounts.schemas import (
    UserSchema,
    UpdateUserInfoSchema,
    UserSignUpSchema,
)
from accounts.models import UserAuthToken

router = Router()
logger = logging.getLogger(__file__)


@router.get('/', response=UserSchema)
def get_user_info(request):
    '''
    Returns information about the current logged-in user.
    '''
    return request.auth


@router.put('/')
def update_user_info(request, body: UpdateUserInfoSchema):
    '''
    Updates information about a user.
    '''
    # TODO: Implement me


@router.post('/login', auth=None)
def user_log_in(request, username: str, password: str):
    '''
    Creates an authentication token for users to use in subsequent requests
    to identify themselves with the application.
    '''
    user = authenticate(username=username, password=password)

    response = {}

    if not user:
        response['success'] = False
        response['detail'] = 'Login failed, please provide correct creds'
    else:
        # Create an authentication token
        token = UserAuthToken.objects.create(user=user)

        response['success'] = True
        response['detail'] = 'Successfully logged in'
        response['auth_token'] = str(token.key)

    return response


@router.post('/sign-up', auth=None)
def user_sign_up(request, body: UserSignUpSchema):
    '''
    Creates a user account.
    '''
    user = User.objects.create_user(
        username=body.username,
        password=body.password,
        email=body.email,
        first_name=body.first_name,
        last_name=body.last_name
    )

    user.save()
    response = {
        'success': True,
        'detail': 'Successfully created a user',
    }

    return response

from ninja import Router
import logging

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from accounts.schemas import (
    UserSchema,
    UpdateUserInfoSchema,
    UserLoginSchema,
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
    user = request.auth
    changed_fields = []

    if body.password:
        # Passwords are hashed under the hood, so we need to
        # update it separately
        user.set_password(body.password)
        changed_fields.append('password')

    if body.firstname:
        user.first_name = body.firstname
        changed_fields.append('firstname')

    if body.lastname:
        user.last_name = body.lastname
        changed_fields.append('lastname')

    # Save changes to the currently authenticated user
    user.save()

    formatted_changes = ', '.join(changed_fields)
    response = {
        'success': True,
        'detail': f'Successfully changed: {formatted_changes}'
    }

    return response


@router.delete('/')
def delete_user(request):
    '''
    Deletes the currently logged-in user and all sessions by
    cascading deletes.
    '''
    username = request.auth.username
    request.auth.delete()

    response = {
        'success': True,
        'detail': f'Successfully deleted user {username}'
    }

    return response


@router.post('/login', auth=None)
def user_log_in(request, body: UserLoginSchema):
    '''
    Creates an authentication token for users to use in subsequent requests
    to identify themselves with the application.
    '''
    user = authenticate(username=body.username, password=body.password)

    response = {}

    if not user:
        response['success'] = False
        response['detail'] = 'Login failed, please provide correct creds'
    else:
        # Create an authentication token
        token = UserAuthToken.objects.create(user=user)

        response['success'] = True
        response['detail'] = 'Successfully logged in'
        response['token'] = str(token.key)

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
        first_name=body.firstname,
        last_name=body.lastname
    )

    user.save()
    response = {
        'success': True,
        'detail': 'Successfully created a user',
    }

    return response

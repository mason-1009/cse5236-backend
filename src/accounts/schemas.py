from ninja import Schema, Field


class UserSchema(Schema):
    # Returns information about a user
    username: str
    email: str
    firstname: str = Field(..., alias='first_name')
    lastname: str = Field(..., alias='last_name')


class UpdateUserInfoSchema(Schema):
    # All fields are optional
    password: str = None
    firstname: str = None
    lastname: str = None


class UserLoginSchema(Schema):
    username: str
    password: str


class UserSignUpSchema(Schema):
    # Base Django user fields
    username: str
    password: str
    email: str
    firstname: str
    lastname: str

    # TODO: Additional fields for linked object

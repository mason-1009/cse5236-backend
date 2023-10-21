from ninja import Schema


class UserSchema(Schema):
    # Returns information about a user
    username: str
    email: str
    first_name: str
    last_name: str


class UpdateUserInfoSchema(Schema):
    # All fields are optional
    password: str = None
    first_name: str = None
    last_name: str = None


class UserLoginSchema(Schema):
    username: str
    password: str


class UserSignUpSchema(Schema):
    # Base Django user fields
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

    # TODO: Additional fields for linked object

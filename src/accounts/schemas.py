from ninja import Schema


class UserSchema(Schema):
    # Returns information about a user
    username: str
    email: str
    firstname: str
    lastname: str


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

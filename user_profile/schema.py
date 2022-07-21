from ninja import ModelSchema, Schema

from .models import User


class UserRegisterSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['firstname', 'lastname', 'username', 'email', 'password', 'phone']


class UserGetSchema(ModelSchema):
    class Config:
        model = User
        model_fields = [
            'id',
            'firstname',
            'lastname',
            'username',
            'email',
            'phone',
            'address',
            'about',
            'image',
        ]


class UserPutSchema(ModelSchema):
    class Config:
        model = User
        model_fields = [
            'firstname',
            'lastname',
            'username',
            'email',
            'phone',
            'address',
            'about',
        ]


class MessageSchema(Schema):
    message: str

from ninja import ModelSchema, Schema

from .models import ProfileUser
from django.contrib.auth.models import User

class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['first_name', 'last_name','username', 'email' ]
        # model_fields = '__all__'
class GetProfileSchema(ModelSchema):
    user: UserSchema = None
    class Config:
        model = ProfileUser
        model_fields = '__all__'

class ProfileUserPutSchema(ModelSchema):
    class Config:
        model = ProfileUser
        model_fields = ['phone','address','about']

class ResponsePutSchema(ModelSchema):
    user: UserSchema = None
    class Config:
        model = ProfileUser
        model_fields = '__all__'
        
class MessageSchema(Schema):
    message: str

from ninja import ModelSchema
from django.contrib.auth.models import User

class CreateUserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['username', 'password', 
                        'email', 'first_name',
                        'last_name']

class LoginUserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['username', 'password']
  

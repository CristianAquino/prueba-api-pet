from typing import List

# from django.contrib.auth import authenticate
# from django.http import JsonResponse
from ninja import Router

from .models import User
from .schema import MessageSchema, UserGetSchema, UserPutSchema, UserRegisterSchema

# from ninja.errors import HttpError


router = Router()


@router.get('/', auth=None, response=List[UserGetSchema])
def get_all(request):
    users = User.objects.all()
    return users


@router.get('/{id}', auth=None, response={200: UserGetSchema, 404: MessageSchema})
def get_one(request, id: int):
    try:
        profile = User.objects.get(pk=id)
        return 200, profile
    except User.DoesNotExist:
        return 404, {'message': 'Datos no encontrados'}


@router.post('/', auth=None, response=UserRegisterSchema)
def post_one(request, pr: UserRegisterSchema):
    profile = User.objects.create(**pr.dict())
    return profile


@router.put('/{id}', auth=None, response={200: UserPutSchema, 404: MessageSchema})
def put_one(request, id: int, data: UserPutSchema):
    try:
        profile = User.objects.get(pk=id)
        for k, v in data.dict().items():
            setattr(profile, k, v)
        profile.save()
        return 200, profile
    except User.DoesNotExist:
        return 404, {'message': 'Datos no encontrados'}


@router.delete('/{id}', auth=None, response={200: None, 404: MessageSchema})
def profile_delete(request, id: int):
    try:
        profile = User.objects.get(pk=id)
        profile.delete()
        return 200
    except User.DoesNotExist:
        return 404, {'message': 'Datos no encontrados'}

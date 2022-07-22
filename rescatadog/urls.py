from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from ninja import NinjaAPI
from ninja.security import HttpBearer

from adoptions.api import router as adoptions_router
from auth.api import router as auth_router
from auth.token import verify_token
from pet_management.api import router as pet_management_router
from user_profile.api import router as user_profile_router
# agregado
from prueba.api import router as prueba_router


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        em = verify_token(token)
        user = User.objects.filter(email=em).first()
        if user is not None:
            return token


api = NinjaAPI(version='1.0.0', auth=GlobalAuth())


@api.get('/', summary='Hello api 1.00', description='API 1.00')
def add(request):
    return {'message': 'Hello api 1.00'}


api.add_router('/auth/', auth_router, tags=['auth'])
api.add_router('/adoptions/', adoptions_router, tags=['adoptions'])
api.add_router('/pets/', pet_management_router, tags=['Pet Management'])
# api.add_router('/user/', user_profile_router, tags=['user'])
api.add_router('/user/profile/', prueba_router, tags=['profile'])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

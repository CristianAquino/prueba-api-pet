from ninja import ModelSchema

from .models import Pet, PetCategory, PetProfile


class CreatePetCategorySchema(ModelSchema):
    class Config:
        model = PetCategory
        model_fields = ['name']


class ResponsePetCategorySchema(ModelSchema):
    class Config:
        model = PetCategory
        model_fields = '__all__'


class ResponsePetProfileSchema(ModelSchema):
    class Config:
        model = PetProfile
        model_fields = '__all__'


class CreatePetSchema(ModelSchema):
    gender: str
    age: int
    location: str
    class Config:
        model = Pet
        model_fields = [
            'name',
            'description',
            'url',
            'pet_category'
        ]


class ResponsePetSchema(ModelSchema):
    pet_category: ResponsePetCategorySchema = None
    pet_profile: ResponsePetProfileSchema = None
    class Config:
        model = Pet
        model_fields = '__all__'

#agregado
class ResponsePetSearch(ModelSchema):
    pet_profile: ResponsePetProfileSchema
    class Config:
        model= Pet
        model_fields = ['name','url']
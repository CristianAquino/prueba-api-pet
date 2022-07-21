from adoptions.models import *
from ninja import Router

from adoptions.schema import CreateAdoptionSchema

router = Router()

@router.post('/',auth=None, summary="Register Adoption",description="Fill" )
def registerAdoption(request,payload: CreateAdoptionSchema):
    Adoption.objects.create(**payload.dict())
    return {"message":"Adoption registered"}
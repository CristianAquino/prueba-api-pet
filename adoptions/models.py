from datetime import datetime
from django.db import models

class Adoption(models.Model):
    adopter_id = models.IntegerField()
    pet_id = models.IntegerField()
    rescuer_id = models.IntegerField()
    created_at=models.DateTimeField(auto_now=datetime.now)
    updated_at=models.DateTimeField()
    deleted=models.BooleanField(auto_created=False)

class AdoptionDetail(models.Model):
    adoption_id = models.IntegerField()
    rescuer_id = models.IntegerField()
    created_at=models.DateTimeField(auto_now=datetime.now)
    updated_at=models.DateTimeField()
    deleted=models.BooleanField(auto_created=False)
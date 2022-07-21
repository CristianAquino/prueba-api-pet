from datetime import datetime
from django.db import models


class PetCategory(models.Model):
    name = models.CharField(max_length=180)
    created_at=models.DateTimeField(auto_now=datetime.now)
    updated_at=models.DateTimeField(null=True)
    deleted=models.BooleanField(auto_created=False)


class PetProfile(models.Model):
    gender = models.CharField(max_length=60)
    age = models.IntegerField()
    location = models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now=datetime.now)
    updated_at=models.DateTimeField(null=True)
    deleted=models.BooleanField(auto_created=False)


class Pet(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField()
    url = models.URLField(null=True)
    is_adopted = models.BooleanField(default=False)
    pet_category = models.ForeignKey(
        PetCategory,
        on_delete=models.CASCADE
    )
    pet_profile = models.ForeignKey(
        PetProfile,
        on_delete=models.CASCADE
    )
    created_at=models.DateTimeField(auto_now=datetime.now)
    updated_at=models.DateTimeField(null=True)
    deleted=models.BooleanField(auto_created=False)

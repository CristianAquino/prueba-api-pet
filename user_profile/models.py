from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=100, default='No registra ubicacion')
    about = models.CharField(max_length=200, default='No registra descripcion')
    image = models.URLField(
        default='https://cdn.pixabay.com/photo/2018/04/18/18/56/user-3331256_960_720.png',
    )
    creation = models.DateTimeField(auto_now_add=True)
    is_superuser = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)

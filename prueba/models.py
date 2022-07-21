from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileUser(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE,null=False,blank=False)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=250, default='No registra ubicacion')
    about = models.CharField(max_length=250, default='No registra descripcion')
    image = models.URLField(
        default='https://cdn.pixabay.com/photo/2018/04/18/18/56/user-3331256_960_720.png',
    )
    creation = models.DateTimeField(auto_now_add=True)
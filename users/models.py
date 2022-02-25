from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  
   
   email = models.EmailField(unique=True)
   saldo = models.IntegerField(default= 1000)

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []


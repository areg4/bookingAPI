from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    
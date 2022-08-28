from django.db import models
from modules.business.models import Business

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=250)
    capacity = models.IntegerField(null=False, blank=False)
    created_by = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
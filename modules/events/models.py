from django.db import models
from modules.rooms.models import Rooms
from modules.business.models import Business

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=250)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    event_date = models.DateField(null=False, blank=False)
    available = models.BooleanField(default=True)
    created_by = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
from django.db import models
from modules.customers.models import Customers
from modules.events.models import Events

# Create your models here.
class Books(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
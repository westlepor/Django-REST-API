import uuid
from django.db import models

# Create your models here.
class Customer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, 
        editable=False, unique=True, db_index=True)
    email = models.EmailField(
        max_length=255,
        unique=True,        
        blank=False,
        verbose_name='email'
    )
    password = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='password'
    )

class Device(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, 
        editable=False, unique=True, db_index=True)    
    device_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='device_id'
    )
    customer = models.ForeignKey(Customer, related_name='device', on_delete=models.CASCADE)

class Task(models.Model):
    _id = models.IntegerField()
    state = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='state'
    )
    customer = models.ForeignKey(Customer, related_name='task', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, related_name='task', on_delete=models.CASCADE)
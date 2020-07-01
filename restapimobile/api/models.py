import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    device_id = models.UUIDField(
        unique=True,
        verbose_name='device_id'
    )
    customer = models.ForeignKey(Customer, related_name='device', on_delete=models.CASCADE)

class Task(models.Model):
    task_id = models.IntegerField(
        blank=False,
        unique=True,
        verbose_name='id'
    )
    state = models.IntegerField(
        # 0 means available task
        default=0,
        blank=False,
        verbose_name='state'
    )
    executed = models.BooleanField(
        default=False,
        verbose_name='execute'
    )
    result = models.IntegerField(
        default=-1,
        validators=[MinValueValidator(0), MaxValueValidator(2)],
        blank=False,
        verbose_name='result'
    )
    customer = models.ForeignKey(Customer, related_name='task', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, related_name='task', on_delete=models.CASCADE)
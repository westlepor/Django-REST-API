from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Device, Task
from .serializers import CusotmerSerializer, DeviceSerializer, TaskSerializer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    lookup_field='uuid'
    queryset=Customer.objects.all()
    serializer_class = CusotmerSerializer

    
class DeviceViewSet(viewsets.ModelViewSet):
    lookup_field='uuid'
    queryset=Device.objects.all()
    serializer_class = DeviceSerializer

    
class TaskViewSet(viewsets.ModelViewSet):
    lookup_field='uuid'
    queryset=Task.objects.all()
    serializer_class = TaskSerializer
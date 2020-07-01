from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import F

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

class AvailableTaskView(APIView):
    def get(self, request, *args, **kwargs):
        device_id = self.kwargs['device_id']
        tasks = Task.objects.filter(device=device_id)
        task_ids = []
        states = []
        for task in tasks:
            task_id = Task._meta.get_field('task_id').value_from_object(task)
            state = Task._meta.get_field('state').value_from_object(task)
            # 0 means that task can execute            
            if state == 0:
                task_ids.append(task_id)
                states.append(state)
            
        return Response({
            'task_id':task_ids,
            'state':states
        })

class ExecutedTaskView(APIView):
    def get(self, request, *args, **kwargs):
        device_id = self.kwargs['device_id']
        task_id = self.kwargs['task_id']
        task = Task.objects.get(device=device_id, task_id=task_id)
        success = False
        try:
            task.executed = True
            task.save()
            success = True
        except:
            pass
        return Response({
            'success':success,
        })

class ResultTaskView(APIView):
    def get(self, request, *args, **kwargs):
        device_id = self.kwargs['device_id']
        task_id = self.kwargs['task_id']
        result = self.kwargs['result']
        task = Task.objects.get(device=device_id, task_id=task_id)
        success = False
        try:
            task.result = result
            task.save()
            success = True
        except:
            pass
        return Response({
            'success':success,
        })
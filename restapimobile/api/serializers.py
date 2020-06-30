from rest_framework import serializers
from .models import Customer, Device, Task

class CusotmerSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField()
    class Meta:
        model = Customer
        fields = [
            'email',
            'password',
            'uuid'
        ]

class DeviceSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField()
    class Meta:
        model = Device
        fields = [
            'customer',
            'uuid'
        ]

class TaskSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField()
    class Meta:
        model = Task
        fields = [
            'state',
            'customer',
            'device',
            'uuid'
        ]
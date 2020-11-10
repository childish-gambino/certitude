# serializers.py
from rest_framework import serializers

from .models import HardwareEntitlement

class HardwareEntitlementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HardwareEntitlement
        fields = ('id', 'uuid', 'email', 'computer_name', 'hardware_serial', 'hostname', 'status',)
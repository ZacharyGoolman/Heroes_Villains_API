from rest_framework import serializers
from .models import Super_Types

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Types
        fields = ['id', 'type']
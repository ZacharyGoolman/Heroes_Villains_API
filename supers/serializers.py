from rest_framework import serializers

from supers_types.models import Super_Types
from .models import Supers


class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id','name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'supers_type', 'supers_type_id']
        depth = 1
    supers_type_id = serializers.IntegerField(write_only =True)

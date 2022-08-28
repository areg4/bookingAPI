from dataclasses import field
from rest_framework import serializers
from .models import Rooms


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id','name', 'capacity', 'created_by', 'created_at', 'updated_at']
    
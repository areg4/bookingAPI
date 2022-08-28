from rest_framework import serializers
from .models import Events
import modules.events.services as services


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'name', 'room', 'private', 'event_date', 'available', 'created_by', 'created_at', 'updated_at']
        
        def validate(self, attrs):
            if services.there_is_event_today(attrs['event_date']):
                raise serializers.ValidationError({
                    'event_date': "There is a event today"
                })
            return super().validate(attrs)

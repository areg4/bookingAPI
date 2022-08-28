from rest_framework import serializers
from .models import Books
from modules.events.services import event_is_public
import modules.books.services as services


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'customer', 'event', 'available', 'created_at', 'updated_at']

    def validate(self, attrs):
        if not event_is_public(attrs['event'].id):
            raise serializers.ValidationError({
                'event': "Event is not public!"
            })
            
        if not services.there_is_space(attrs['event'].id):
            raise serializers.ValidationError({
                'event': "Event has not space"
            })
        
        if customer_has_booking(attrs['customer'].id, attrs['event'].id):
            raise serializers.ValidationError({
                "Customer": "You have a booking for this event"
            })
        return super().validate(attrs)
    
    
def customer_has_booking(customer_id, event_id):
    book = Books.objects.filter(customer=customer_id).filter(event=event_id).filter(available=True)
    if book:
        return True
    return False
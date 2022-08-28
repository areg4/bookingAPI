from datetime import date
import logging
from .models import Events
from .serializers import EventsSerializer
from utils.responses import success_response, fail_response
from rest_framework import status


def create_event(data) -> dict:
    try:
        serializer = EventsSerializer(data=data)
        if not serializer.is_valid():
            return fail_response("Fail to create a event", 
                                 status.HTTP_400_BAD_REQUEST, serializer.errors)
        event = Events.objects.create(**serializer.validated_data)
        serializer = EventsSerializer(event)
        return success_response("Event created!", status.HTTP_201_CREATED, serializer.data)
    except Exception as e:
        logging.error("Error to create a Event: {}".format(str(e)))
        return fail_response("Error to create a Event: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
def list_available_events(public=None) -> dict:
    try: 
        events = Events.objects.filter(available=True)
        if public:
            events = events.filter(private=False)
        serializer = EventsSerializer(events, many=True)
        return success_response("List of events", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to list available Events: {}".format(str(e)))
        return fail_response("Error to list available Events: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
def delete_event(event_id) -> dict:
    try: 
        event = Events.objects.filter(id=event_id)
        if not event:
            return fail_response("Event not found", status.HTTP_404_NOT_FOUND)
        event.delete()
        return success_response("Event was deleted", status.HTTP_204_NO_CONTENT)
    except Exception as e:
        logging.error("Error to delete event: {}".format(str(e)))
        return fail_response("Error to delete Event: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        

def disable_event(event_id) -> dict:
    try:
        event = Events.objects.filter(id=event_id)
        if not event:
            return fail_response("Event not found", status.HTTP_404_NOT_FOUND)
        event = event[0]
        event.available = False
        event.save()
        serializer = EventsSerializer(event)
        return success_response("Event disabled", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to disable event: {}".format(str(e)))
        return fail_response("Error to disable Event: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def event_is_public(event_id) -> bool:
    event = Events.objects.filter(id=event_id)
    if event and event[0].private == False:
        return True
    return False


def there_is_event_today(event_date):
    events = Events.objects.filter(event_date=event_date)
    logging.debug(len(events))
    if len(events)>0:
        return True
    return False


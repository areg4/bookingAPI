import logging
from .models import Rooms
from modules.events.models import Events
from .serializers import RoomsSerializer
from utils.responses import success_response, fail_response
from rest_framework import status


def create_room(data) -> dict:
    try:
        serializer = RoomsSerializer(data=data)
        if not serializer.is_valid():
            return fail_response('Fail to create room', 
                                status.HTTP_400_BAD_REQUEST, serializer.errors)
        room = Rooms.objects.create(**serializer.validated_data)
        serializer = RoomsSerializer(room)
        return success_response("Room created!", status.HTTP_201_CREATED, serializer.data)
    except Exception as e:
        logging.error("Error to create a Room: {}".format(str(e)))
        return fail_response("Error to create a Room: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        

def list_of_rooms() -> dict:
    try:
        rooms = Rooms.objects.filter()
        serializer = RoomsSerializer(rooms, many=True)
        return success_response("List of Rooms", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to list Rooms: {}".format(str(e)))
        return fail_response("Error to list Rooms: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
def delete_room(room_id:int) -> dict:
    try:
        room = Rooms.objects.filter(id=room_id)
        if not room:
            return fail_response("Room not found", status.HTTP_404_NOT_FOUND)
        if room_has_events(room_id):
            return fail_response("Room can't be delete because has events availables")
        room.delete()
        return success_response("Room was deleted!", status.HTTP_204_NO_CONTENT)
    except Exception as e:
        logging.error("Error to delete a Room: {}".format(str(e)))
        return fail_response("Error to delete a Room: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
   
        
def room_has_events(room_id) -> bool:
    events = Events.objects.filter(room=room_id).filter(available=True)
    if events:
        return True
    return False

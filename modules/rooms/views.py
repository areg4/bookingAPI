from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_room, list_of_rooms, delete_room


@api_view(['POST'])
def register_room(request):
    create_response = create_room(request.data)
    return Response(data=create_response, status=create_response['status'])


@api_view(['GET'])
def list_rooms(request):
    rooms_response = list_of_rooms()
    return Response(data=rooms_response, status=rooms_response['status'])


@api_view(['DELETE'])
def delete_room_by_id(request, room_id):
    room_delete_response = delete_room(room_id)
    return Response(data=room_delete_response, status=room_delete_response['status'])

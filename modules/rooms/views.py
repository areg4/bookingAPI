from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_room, list_of_rooms, delete_room
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import RoomsSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Register a new Room",
    request_body=RoomsSerializer,
    responses={
        201: "Created",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['POST'])
def register_room(request):
    create_response = create_room(request.data)
    return Response(data=create_response, status=create_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get all Rooms",
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['GET'])
def list_rooms(request):
    rooms_response = list_of_rooms()
    return Response(data=rooms_response, status=rooms_response['status'])


@swagger_auto_schema(
    method='delete',
    operation_description="Delete a Room",
    manual_parameters=[
        openapi.Parameter('room_id', openapi.IN_PATH, 
                          description="room ID", 
                          type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['DELETE'])
def delete_room_by_id(request, room_id):
    room_delete_response = delete_room(room_id)
    return Response(data=room_delete_response, status=room_delete_response['status'])

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_event, list_available_events, delete_event, disable_event
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import EventsSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Register a new Event",
    request_body=EventsSerializer,
    responses={
        201: "Created",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['POST'])
def register_event(request):
    create_response = create_event(request.data)
    return Response(data=create_response, status=create_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get all Public Events",
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['GET'])
def get_public_events(request):
    events_response = list_available_events(True)
    return Response(data=events_response, status=events_response['status'])


@swagger_auto_schema(
    method='delete',
    operation_description="Delete a Event",
    manual_parameters=[
        openapi.Parameter('event_id', openapi.IN_PATH, 
                          description="event ID", 
                          type=openapi.TYPE_INTEGER)
    ],
    responses={
        204: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['DELETE'])
def delete_event_by_id(request, event_id):
    event_deleted_response = delete_event(event_id)
    return Response(data=event_deleted_response, status=event_deleted_response['status'])


@swagger_auto_schema(
    method='patch',
    operation_description="Disable a Event",
    manual_parameters=[
        openapi.Parameter('event_id', openapi.IN_PATH, 
                          description="event ID", 
                          type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['PATCH'])
def disable_event_by_id(request, event_id):
    event_disabled_response = disable_event(event_id)
    return Response(data=event_disabled_response, status=event_disabled_response['status'])

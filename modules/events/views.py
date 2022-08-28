from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_event, list_available_events, delete_event, disable_event


@api_view(['POST'])
def register_event(request):
    create_response = create_event(request.data)
    return Response(data=create_response, status=create_response['status'])


@api_view(['GET'])
def get_public_events(request):
    events_response = list_available_events(True)
    return Response(data=events_response, status=events_response['status'])


@api_view(['DELETE'])
def delete_event_by_id(request, event_id):
    event_deleted_response = delete_event(event_id)
    return Response(data=event_deleted_response, status=event_deleted_response['status'])


@api_view(['PATCH'])
def disable_event_by_id(request, event_id):
    event_disabled_response = disable_event(event_id)
    return Response(data=event_disabled_response, status=event_disabled_response['status'])

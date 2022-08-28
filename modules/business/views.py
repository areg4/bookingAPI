from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_business, get_list_business


@api_view(['POST'])
def register_business(request):
    register_response = create_business(request.data)
    return Response(data=register_response, status=register_response['status'])


@api_view(['GET'])
def list_business(request):
    business_response = get_list_business()
    return Response(data=business_response, status=business_response['status'])

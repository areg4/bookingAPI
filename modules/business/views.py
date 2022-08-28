from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_business, get_list_business
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import BusinessSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Register a new Business",
    request_body=BusinessSerializer,
    responses={
        201: "Created",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['POST'])
def register_business(request):
    register_response = create_business(request.data)
    return Response(data=register_response, status=register_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get all business",
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['GET'])
def list_business(request):
    business_response = get_list_business()
    return Response(data=business_response, status=business_response['status'])

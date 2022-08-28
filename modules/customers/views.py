from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_customer, get_list_cutomers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import CustomersSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Register a new Customer",
    request_body=CustomersSerializer,
    responses={
        201: "Created",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['POST'])
def register_customer(request):
    create_response = create_customer(request.data)
    return Response(data=create_response, status=create_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get all Customers",
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['GET'])
def list_customers(request):
    customers_response = get_list_cutomers()
    return Response(data=customers_response, status=customers_response['status'])

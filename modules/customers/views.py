from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_customer, get_list_cutomers


@api_view(['POST'])
def register_customer(request):
    create_response = create_customer(request.data)
    return Response(data=create_response, status=create_response['status'])


@api_view(['GET'])
def list_customers(request):
    customers_response = get_list_cutomers()
    return Response(data=customers_response, status=customers_response['status'])

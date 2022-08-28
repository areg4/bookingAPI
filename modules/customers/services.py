import logging
from rest_framework import status
from .serializers import CustomersSerializer
from utils.responses import success_response, fail_response
from .models import Customers


def create_customer(data) -> dict:
    try:
        serializer = CustomersSerializer(data=data)
        if not serializer.is_valid():
            return fail_response("Fail to create a customer", 
                                 status.HTTP_400_BAD_REQUEST, serializer.errors)
        Customers.objects.create(**serializer.validated_data)
        return success_response("Customer created!", status.HTTP_201_CREATED, 
                                serializer.validated_data)
    except Exception as e:
        logging.error("Error to create a Customer: {}".format(str(e)))
        return fail_response("Error to create a Customer: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_list_cutomers() -> dict:
    try:
        customers = Customers.objects.filter()
        serializer = CustomersSerializer(customers, many=True)
        return success_response("List customers", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to list Customers: {}".format(str(e)))
        return fail_response("Error to list Customers: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)

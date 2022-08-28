import logging
from rest_framework import status
from .serializers import BusinessSerializer
from utils.responses import success_response, fail_response
from .models import Business


def create_business(data) -> dict:
    try:
        serializer = BusinessSerializer(data=data)
        if not serializer.is_valid():
            return fail_response("Fail to create a business",
                                status.HTTP_400_BAD_REQUEST, serializer.errors)
        Business.objects.create(**serializer.validated_data)
        return success_response("Business created!", status.HTTP_201_CREATED, 
                                serializer.validated_data)
    except Exception as e:
        logging.error("Error to create a Business: {}".format(str(e)))
        return fail_response("Error to create a Business: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def get_list_business() -> dict:
    try:
        business = Business.objects.filter()
        serializer = BusinessSerializer(business, many=True)
        return success_response("List business", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to list Business: {}".format(str(e)))
        return fail_response("Error to list Business: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_book, cancel_booking, get_list_books, get_books_by_customer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import BooksSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Register a new Book",
    request_body=BooksSerializer,
    responses={
        201: "Created",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['POST'])
def register_book(request):
    create_response = create_book(request.data)
    return Response(data=create_response, status=create_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get all books",
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['GET'])
def get_all_books(request):
    books_response = get_list_books()
    return Response(data=books_response, status=books_response['status'])


@swagger_auto_schema(
    method='get',
    operation_description="Get all books by customer",
    manual_parameters=[
        openapi.Parameter('customer_id', openapi.IN_PATH, 
                          description="customer_id ID", 
                          type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['GET'])
def get_customer_books(request, customer_id):
    books_response = get_books_by_customer(customer_id)
    return Response(data=books_response, status=books_response['status'])


@swagger_auto_schema(
    method='delete',
    operation_description="Cancel a booking",
    manual_parameters=[
        openapi.Parameter('customer_id', openapi.IN_PATH, 
                          description="customer_id ID", 
                          type=openapi.TYPE_INTEGER),
        openapi.Parameter('book_id', openapi.IN_PATH, 
                          description="book_id ID", 
                          type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: "OK",
        400: "Bad Request",
        500: "Server Error"
    }
)
@api_view(['DELETE'])
def cancel(request, customer_id, book_id):
    book_response = cancel_booking(customer_id, book_id)
    return Response(data=book_response, status=book_response['status'])

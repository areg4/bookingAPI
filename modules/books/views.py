from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_book, cancel_booking, get_list_books, get_books_by_customer


@api_view(['POST'])
def register_book(request):
    create_response = create_book(request.data)
    return Response(data=create_response, status=create_response['status'])


@api_view(['GET'])
def get_all_books(request):
    books_response = get_list_books()
    return Response(data=books_response, status=books_response['status'])


@api_view(['GET'])
def get_customer_books(request, customer_id):
    books_response = get_books_by_customer(customer_id)
    return Response(data=books_response, status=books_response['status'])


@api_view(['DELETE'])
def cancel(request, customer_id, book_id):
    book_response = cancel_booking(customer_id, book_id)
    return Response(data=book_response, status=book_response['status'])

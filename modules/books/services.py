import logging
from .models import Books
from modules.events.models import Events
from modules.rooms.models import Rooms
from .serializers import BooksSerializer
from utils.responses import success_response, fail_response
from rest_framework import status


def create_book(data) -> dict:
    try:
        serializer = BooksSerializer(data=data)
        if not serializer.is_valid():
            return fail_response("Fail to make a Book", 
                                 status.HTTP_201_CREATED, serializer.errors)
        book = Books.objects.create(**serializer.validated_data)
        serializer = BooksSerializer(book)
        return success_response("Book created!", status.HTTP_201_CREATED, serializer.data)
    except Exception as e:
        logging.error("Error to create a Book: {}".format(str(e)))
        return fail_response("Error to create a Book: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_list_books() -> dict:
    try:
        books = Books.objects.filter(available=True)
        serializer = BooksSerializer(books, many=True)
        return success_response("List of books", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to get books: {}".format(str(e)))
        return fail_response("Error to get books: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_books_by_customer(customer_id):
    try:
        books = Books.objects.filter(customer=customer_id)
        serializer = BooksSerializer(books, many=True)
        return success_response("List of books by customer", status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to get books: {}".format(str(e)))
        return fail_response("Error to get books: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
def cancel_booking(customer_id, book_id):
    try:
        book = Books.objects.filter(customer=customer_id).filter(id=book_id)
        if not book:
            return fail_response("Book not found", 
                                 status.HTTP_404_NOT_FOUND)
        book = book[0]
        book.available = False
        book.save()
        serializer = BooksSerializer(book)
        return success_response("Book canceled", 
                                 status.HTTP_200_OK, serializer.data)
    except Exception as e:
        logging.error("Error to cancel a Book: {}".format(str(e)))
        return fail_response("Error to cancel a Book: {}".format(str(e)), 
                                status.HTTP_500_INTERNAL_SERVER_ERROR)


def there_is_space(event_id):
    event = Events.objects.filter(id=event_id)
    if not event:
        return fail_response("Event not found", 
                                 status.HTTP_404_NOT_FOUND)
    capacity = event[0].room.capacity
    logging.info(capacity)
    bookings = len(Books.objects.filter(event=event_id).filter(available=True))
    logging.info(bookings)
    if bookings < capacity:
        return True
    return False


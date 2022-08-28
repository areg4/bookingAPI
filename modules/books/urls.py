from django.urls import path
from .views import register_book, cancel, get_all_books, get_customer_books

urlpatterns = [
    path('register/', register_book, name="register_book"),
    path('', get_all_books, name="get_all_books"),
    path('<int:customer_id>/', get_customer_books, name='get_customer_books'),
    path('cancel/<int:customer_id>/<int:book_id>/', cancel, name='cancel_book'),
]

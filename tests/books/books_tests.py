import requests
import requests_mock
from django.shortcuts import reverse

URL_REGISTER = 'http://localhost:8080'+ reverse('register_book')
URL_GET_ALL = 'http://localhost:8080'+ reverse('get_all_books')
URL_GET_CUSTOMER_BOOKS = 'http://localhost:8080'+ reverse('get_customer_books', kwargs={'customer_id':1})
URL_CANCEL_BOOK = 'http://localhost:8080'+ reverse('cancel_book', kwargs={'customer_id':1, 'book_id': 4})


def test_register_book(mocker, mock_register_body, mock_register_reponse):
    mocker.patch(
        'modules.books.services.create_book',
        return_value=mock_register_reponse
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_REGISTER, json=mock_register_reponse)
        response = requests.post(URL_REGISTER, data=mock_register_body)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 201
    assert response_json['data'] is not None


def test_get_all_books(mocker, mock_get_all_books):
    mocker.patch(
        'modules.books.services.get_list_books',
        return_value=mock_get_all_books
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_GET_ALL, json=mock_get_all_books)
        response = requests.get(URL_GET_ALL)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    assert response_json['data'] is not None
    

def test_get_books_by_cutomer(mocker, mock_get_books_by_cutomer):
    mocker.patch(
        'modules.books.services.get_list_books',
        return_value=mock_get_books_by_cutomer
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_GET_CUSTOMER_BOOKS, json=mock_get_books_by_cutomer)
        response = requests.get(URL_GET_CUSTOMER_BOOKS)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    assert response_json['data'] is not None
    

def test_cancel_book(mocker, mock_cancel_book):
    mocker.patch(
        'modules.books.services.cancel_booking', 
        return_value= mock_cancel_book
    )
    
    with requests_mock.Mocker() as m:
        m.delete(URL_CANCEL_BOOK, json=mock_cancel_book)
        response = requests.delete(URL_CANCEL_BOOK)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    

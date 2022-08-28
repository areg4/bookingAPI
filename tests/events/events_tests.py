import json
from urllib import response
import requests
import requests_mock
from django.shortcuts import reverse

URL_REGISTER = 'http://localhost:8080'+ reverse('register_event')
URL_GET_ALL_PUBLIC = 'http://localhost:8080'+ reverse('list_puublic_events')
URL_DELETE_EVENT = 'http://localhost:8080'+ reverse('delete_event_by_id', kwargs={'event_id':1})
URL_DISABLE_EVENT = 'http://localhost:8080'+ reverse('disable_event_by_id', kwargs={'event_id':1})

def test_register_event(mocker, mock_register_body, mock_register_response):
    mocker.patch(
        'modules.events.services.create_event',
        return_value=mock_register_response
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_REGISTER, json=mock_register_response)
        response = requests.post(URL_REGISTER, data=mock_register_body)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 201
    assert response_json['data'] is not None
    
    
def test_get_all_public_events(mocker, mock_get_public_events):
    mocker.patch(
        'modules.events.services.list_available_events',
        return_value=mock_get_public_events
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_GET_ALL_PUBLIC, json=mock_get_public_events)
        response = requests.get(URL_GET_ALL_PUBLIC)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    assert response_json['data'] is not None


def test_delete_event(mocker, mock_delete_event):
    mocker.patch(
        'modules.events.services.delete_event',
        return_value=mock_delete_event
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_DELETE_EVENT, json=mock_delete_event)
        response = requests.get(URL_DELETE_EVENT)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 204
    

def test_disable_event(mocker, mock_disable_event):
    mocker.patch(
        'modules.events.services.delete_event',
        return_value=mock_disable_event
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_DISABLE_EVENT, json=mock_disable_event)
        response = requests.get(URL_DISABLE_EVENT)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200

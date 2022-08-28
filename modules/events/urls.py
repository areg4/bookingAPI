from django.urls import path
from .views import register_event, get_public_events, disable_event_by_id, delete_event_by_id

urlpatterns = [
    path('register/', register_event, name="register_event"),
    path('public/', get_public_events, name="list_puublic_events"),
    path('<int:event_id>/', delete_event_by_id, name='delete_event_by_id'),
    path('disable/<int:event_id>/', disable_event_by_id, name='disable_event_by_id'),
]

from django.urls import path
from .views import register_room, list_rooms, delete_room_by_id

urlpatterns = [
    path('register/', register_room, name="register_room"),
    path('', list_rooms, name="list_rooms"),
    path('<int:room_id>/', delete_room_by_id, name='delete_room_by_id'),
]

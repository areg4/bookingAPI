from django.urls import path
from .views import register_business, list_business

urlpatterns = [
    path('register/', register_business, name="register_business"),
    path('', list_business, name="register_business"),
]
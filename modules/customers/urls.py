from django.urls import path
from .views import register_customer, list_customers

urlpatterns = [
    path('register/', register_customer, name="register_business"),
    path('', list_customers, name="register_business"),
]
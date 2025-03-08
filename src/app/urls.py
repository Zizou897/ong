from django.urls import path
from .views import (
    home,
    contact,
)

urlpatterns = [
    path('', home, name='welcome'),
    path('contact', contact, name='contact'),
]
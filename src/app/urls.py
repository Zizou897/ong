from django.urls import path
from .views import (
    home,
    contact,
    cas,
    about,
)

urlpatterns = [
    path('', home, name='welcome'),
    path('contact', contact, name='contact'),
    path('cas', cas, name='cas'),
    path('a-props', about, name='about'),
]
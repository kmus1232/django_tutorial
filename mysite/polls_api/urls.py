from django.urls import path
from .views import *

urlpatterns = [
    path('questions/', question_list, name='question_list'),
]
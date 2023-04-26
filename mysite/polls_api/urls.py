from django.urls import path
from .views import *

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<int:id>/', question_detail, name='question_detail'),
]

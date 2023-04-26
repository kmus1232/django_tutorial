from django.urls import path
from .views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question_detail'), # GenericAPIView는 pk를 기본키로 사용하기 때문에 pk를 사용해야 한다.
]

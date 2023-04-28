from rest_framework import serializers
from polls.models import Question
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = "__all__"
        fields = ["id", "question_text", "pub_date"]
        
        
class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    # User 모델에 질문이 없기 때문에 질문 테이블을 따로 불러와야 한다.

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']
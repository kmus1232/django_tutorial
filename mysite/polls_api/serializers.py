from rest_framework import serializers
from polls.models import Question
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


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
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "두 패스워드가 일치하지 않습니다."})
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])    
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
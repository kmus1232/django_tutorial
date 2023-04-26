from django.shortcuts import get_object_or_404
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView


class QuestionList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QuestionDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # RetrieveModelMixin

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # UpdateModelMixin

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # DestroyModelMixin

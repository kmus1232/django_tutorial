import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="질문")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    # auto_now : 객체가 변경될 때마다 현재 시간으로 자동으로 저장
    # auto_now_add : 객체가 생성될 때만 현재 시간으로 자동으로 저장

    @admin.display(boolean=True, description="최근 생성(하루 기준)")
    def was_published_recently(self):
        # 게시된지 1일 이내인지 확인
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        if self.was_published_recently():
            new_badge = "🆕"
        else:
            new_badge = ""
        return f"{new_badge} {self.question_text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"[{self.question.question_text}] {self.choice_text}"

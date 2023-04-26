from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('질문 섹션', {'fields': ['question_text']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text', 'choice__choice_text'] # Question.objects.filter(choice__choice_text='~' //__startswith='아니오')


# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

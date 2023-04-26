from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'questions': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "선택한 항목이 없습니다."
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    most_voted_choice = choices.order_by('-votes')[0]
    context = {
        "question": question,
        "most_voted_choice": most_voted_choice,
    }
    return render(request, 'polls/result.html', context)

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

def home_page(request):
    question = Question.objects.all()
    return render(request,'quiz/home.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/detail.html'

def add_question(request):
    question = Question.objects.all
    new_question = Question.objects.create(question_text = request.POST['q_in'])
    return redirect('/')


def add_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.choice_set.create(choice_text = request.POST['c_in'], votes=0) 
    return render(request,'quiz/detail.html', {'question': question})


def del_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('/')

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'quiz/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))


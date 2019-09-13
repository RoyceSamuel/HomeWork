from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404
from quiz.blogic.questions_reader import reader
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import json
import functools
from django.contrib.sessions.backends.db import SessionStore


def signup(request):
    context = {}    
    if request.method=="POST":
        f_user_form = UserCreationForm(request.POST)
        if f_user_form.is_valid():
            f_user_form.save()
            return render(request, 'quiz/index.html', {})
    else:
        f_user_form= UserCreationForm()
        context = {
        'form': f_user_form,
        }
        return render(request, 'quiz/signup.html', context)

def index(request):
    latest_question_list = []
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'quiz/index.html', context)

def load_random_question():
    dict_from_file = reader.question_reader
    latest_question_list = dict_from_file.read_json_file() 
    questions = latest_question_list[0:10]
    return questions

@login_required
def start_quiz(request):
    questions = load_random_question()
    request.session['questions']  = questions
    request.session['users_answers'] ={}
    context = {
        'users_answers': None,
        'latest_question_list': [questions[0]],
        'next_question' : 1,
        'length_of_dataset': len(questions),
    }
    request.session['context'] =context
    return render(request, 'quiz/startquiz.html', context)

@login_required
def startquizmonitor(request,page_id):
    questions = request.session['questions']
    x = request.session['users_answers']
    if request.method=="POST":
        question_id = request.POST['question_id']       
        x.update(
             {
                 question_id : request.POST.getlist('q_answers')
             })
        request.session['users_answers'] = x 
    
    print(request.session['users_answers'])

    if page_id == len(questions) :
        return render(request, 'quiz/results.html', 
                context={
                'users_answers': request.session['users_answers'],
                'latest_question_list': questions,
                'next_question' : 0,
                'length_of_dataset': len(questions),
                }
        )

    context = {
        'users_answers': None,
        'latest_question_list': [questions[page_id]],
        'next_question' : page_id + 1,
        'length_of_dataset': len(questions),
    }
    return render(request, 'quiz/startquizmonitor.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % request.POST['usrname'])

def vote_clear(request, question_id):
    return HttpResponse("You're voting the clear page on question %s." % request.POST['usrname'])

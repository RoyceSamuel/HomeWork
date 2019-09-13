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

x={}
part_latest_list = None

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

@login_required
def start_quiz(request):
    dict_from_file = reader.question_reader
    latest_question_list = dict_from_file.read_json_file() 
    questions = latest_question_list[0:6]

    page = request.GET.get('page',1)
    paginator = Paginator(questions, 1)

    try:
        part_latest_list = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        part_latest_list = paginator.page(paginator.num_pages)
    
    # print(page,part_latest_list)
    
    if request.method=="POST":        
        question_id = request.POST['question_id']
        x.update(
             {
                 question_id : request.POST.getlist('q_answers')
             })
        print(x)
        part_latest_list = paginator.page(page)
    
    # if int(page)>=len(paginator.page_range):
    #      return render(request, 'quiz/results.html', {
    #          'users_answers': x,
    #          'latest_question_list':questions
    #      })

    context = {
        'users_answers': None,
        'latest_question_list': part_latest_list,
    }
    
    return render(request, 'quiz/startquiz.html', context)

def startquiz(request,question_id):
    if request.method=="POST":
        print(request.POST)
        print("QuestionID  :",question_id)
        latest_question_list=None
        context = {
                'latest_question_list': latest_question_list,
            }
    return render(request, 'quiz/startquiz.html', context)


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

from django.shortcuts import render

# Create your views here.
#creating my first http response
from django.http import HttpResponse

from .models import Question
#def index(request):
#    return HttpResponse("Hello Welcome to Python Server")
def index(request):
    latest_questions_list=Question.objects.order_by("pub_date")[:5]
    output=",".join([q.question_text for q in latest_questions_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse("You're looking at question %s"%question_id)

def results(request,question_id):
    response="You are looking at the result of the questions uploaded %s"
    return HttpResponse(response,question_id)

def vote(request,question_id):
    return HttpResponse("you're voting on the question %s"%question_id)


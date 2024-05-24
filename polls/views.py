from django.shortcuts import get_object_or_404,render
from django.http import Http404
# Create your views here.
#creating my first http response
from django.http import HttpResponse

from .models import Question

from django.template import loader

#def index(request):
#    return HttpResponse("Hello Welcome to Python Server")
def index(request):
    latest_questions_list=Question.objects.order_by("pub_date")[:5]
    template=loader.get_template(".polls/index.html")
    context={
        "latest_question_list":latest_questions_list
    }
    #output=",".join([q.question_text for q in latest_questions_list])
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not exist")
    return render(request,'polls/detail.html',{"question":Question})
    #return HttpResponse("You're looking at question %s"%question_id)

def results(request,question_id):
    response="You are looking at the result of the questions uploaded %s"
    return HttpResponse(response,question_id)

def vote(request,question_id):
    return HttpResponse("you're voting on the question %s"%question_id)


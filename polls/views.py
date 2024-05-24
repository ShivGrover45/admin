from django.shortcuts import get_object_or_404,render
from django.http import Http404
# Create your views here.
#creating my first http response
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question

from django.template import loader

from django.db.models import F
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
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{"question":question})
    #return HttpResponse("You're looking at question %s"%question_id)

def results(request,question_id):
    response="You are looking at the result of the questions uploaded %s"
    return HttpResponse(response,question_id)

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,question.DoesNotExist):
        return render(request,
                      "polls/index.html",
                      {
                          "question":question,
                                              "error_message":"You didn't select a question"                    })
    else:
        selected_choice.votes=F("votes")+1;
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question_id)))
    


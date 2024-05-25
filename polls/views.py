from django.shortcuts import get_object_or_404,render
from django.http import Http404
# Create your views here.
#creating my first http response
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question

from django.template import loader
from django.views import generic
from django.db.models import F
#def index(request):
#    return HttpResponse("Hello Welcome to Python Server")
class indexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="latest_questions_list"
    def get_queryset(self):
        return Question.objects.order_by("pub_date")[:5]
    
    
class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"

class ResultsView(generic.DetailView):
    model=Question
    template_name="poll/results.html"


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
    


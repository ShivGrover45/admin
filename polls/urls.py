from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_View(), name='index'),
    path("<int:question_id>/",views.DetailView.as_View(),name="detail"),
    path("<int:question_id>/results",views.ResultsView.as_View(),name="results"),
    path("<int:question_id>/votes",views.vote,name="vote"),
]
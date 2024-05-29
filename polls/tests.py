import datetime
from polls.models import Question
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.test import Client
client=Client()
class QuestionModelTest(TestCase):

    def test_was_published_recently_with_old_question(self):
        time=timezone.now()-datetime.timedelta(days=1,seconds=1)
        old_question=Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        time=timezone.now()-datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question=Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),False)   

    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),True)


# Create your tests here.
def create_question(question_text,days):
    time=timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response=self.client.get("polls:index")
        self.assertEquals(response.status_code,200)
        self.assertContains("No poles are available")
        self.assertQuerySetEqual(response.context["latest_question_text"],[])
    def test_past_question(self):
        question=create_question(question_text="Past questions.",days=-30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_text"],[question]
        )
    def test_future_question(self):  
        create_question(question_text="Future Question",days=30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_text"],[]
        )
    def test_future_and_past_question    
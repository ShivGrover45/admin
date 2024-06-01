from django.contrib import admin
from .models import Choice,Question
 
class choiceInline(admin.TabularInline):
    model=Choice
    extra=3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{"fields":["question_text"]}),
               ("Date Information",{"fields":["pub_date"]})]
    inlines=[choiceInline]
    list_display=["question_text","pub_date","was_published_recently"]

admin.site.register(Question,QuestionAdmin)
# Register your models here.

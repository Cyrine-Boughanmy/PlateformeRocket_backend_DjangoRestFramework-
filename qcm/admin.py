from django.contrib import admin
from .models import *

class AnswerQuestion(admin.ModelAdmin):
    list_filter = ['question']

class QuestionQcm(admin.ModelAdmin):
    list_filter = ['qcm']

admin.site.register(Qcm)
admin.site.register(Question, QuestionQcm)
admin.site.register(Answer, AnswerQuestion)
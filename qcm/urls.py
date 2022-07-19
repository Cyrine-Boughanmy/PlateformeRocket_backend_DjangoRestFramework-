from django import views
from django.urls import path
from .views import * 

urlpatterns = [
    path('qcmCreate/', ListCreateQcm.as_view(), name='qcm_list'),
    path(r'^(?P<pk>\d+)/$', RetrieveUpdateDestroyQcm.as_view(), name='qcm_details'),
    path(r'^(?P<quiz_pk>\d+)/questions/$', ListCreateQuestion.as_view(), name='question_list'),
    path(r'^(?P<quiz_pk>\d+)/questions/(?P<pk>\d+)/$', RetrieveUpdateDestroyQuestion.as_view(), name='question_details'),
    path(r'^(?P<quiz_pk>\d+)/questions/(?P<question_pk>\d+)/answers/$', ListCreateAnswer.as_view(), name='answer_list'),
    path(r'^(?P<quiz_pk>\d+)/questions/(?P<question_pk>\d+)/answers/(?P<pk>\d+)/$', RetrieveUpdateDestroyAnswer.as_view(), name='answer_details'),

]

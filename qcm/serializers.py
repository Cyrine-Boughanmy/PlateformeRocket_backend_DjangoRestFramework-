from .models import *
from rest_framework import serializers

class QcmSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='apiv2:question-detail')

    def getQuestionCount(self, obj):
        return obj.question_count 

    question_count = serializers.SerializerMethodField("getQuestionCount")

    class Meta:
        model = Qcm
        fields = [
            'id',
            'nom',
            'categorie',
            'questions'
        ]

class AnswerSerializer(serializers.ModelSerializer):
    model = Answer
    fields = [
        'id',
        'text',
        'correct'
    ]

class QuestionSerializer(serializers.ModelSerializer):
    qcm_nom = serializers.CharField(source='qcm.nom', read_only = True)
    answers = AnswerSerializer(read_only = True, many = True)

    class Meta:
        model = Question
        fields = [
            'id',
            'qcm_nom',
            'prompt',
            'answers'
        ]
        
# class QcmSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Qcm
#         fields = '__all__'
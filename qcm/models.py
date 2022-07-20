from django.db import models
from categories.models import Categorie
class Qcm(models.Model):
    nom = models.CharField(max_length=45)
    categorie = models.ManyToManyField(Categorie, null=True)

    @property
    def question_count(self):
        return self.questions.count()
    class Meta: 
        verbose_name_plural = "Qcm"
        ordering = ['id']
    
    def __str__(self):
        return self.nom

class Question(models.Model):
    qcm = models.ForeignKey(Qcm, related_name='questions', on_delete=models.DO_NOTHING)
    choix_reponses = models.CharField(max_length=255, default ='')

    class Meta: 
        ordering = ['id']

    def __str__(self):
        return self.choix_reponses

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.DO_NOTHING)
    reponse = models.CharField(max_length=255)
    correct = models.BooleanField(default = False)
    score = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.reponse 


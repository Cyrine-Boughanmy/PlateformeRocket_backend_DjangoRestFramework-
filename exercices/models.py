from django.db import models
from cours.models import Cours
'''
This is a model for the plateform's exercices 
'''
class Exercices(models.Model):
    nom = models.CharField(max_length=45)
    cours = models.ManyToManyField(Cours, null=True)
    enonce =  models.CharField(max_length=10)
    bonne_reponse = models.CharField(max_length=45) 
    

from django.db import models

'''
This is model for the plateform's Courses 
'''
class Cours(models.Model):
    nom = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    catégorie =  models.CharField(max_length=10)
    titre_module = models.CharField(max_length=45) 
    cours_module = models.CharField(max_length=45) 
    valeur_init = models.IntegerField(blank=True, null=True)

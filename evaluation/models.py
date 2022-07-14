from django.db import models
from categories.models import Categorie

class EvaluationClass(models.Model):
    titre = models.CharField(max_length=45)
    enonce = models.CharField(max_length=100)
    lien = models.CharField(max_length=45)
    fichier_pdf = models.FileField()
    categorie = models.ManyToManyField(Categorie, null=True)

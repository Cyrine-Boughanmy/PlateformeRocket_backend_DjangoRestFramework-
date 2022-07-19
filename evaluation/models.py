from django.db import models
from categories.models import Categorie

class EvaluationClass(models.Model):
    titre = models.CharField(max_length=45)
    enonce = models.TextField(max_length=100)
    lien = models.URLField(max_length=200)
    fichier_pdf = models.FileField(upload_to='file_uploads/evalutions/', blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True, null=True, related_name='evaluations')

    def __str__(self):
        return self.titre 
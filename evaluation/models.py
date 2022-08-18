from django.db import models
from categories.models import Categorie
from ckeditor.fields import RichTextField
class EvaluationClass(models.Model):
    titre_evaluation = models.CharField(max_length=45)
    enonce_evaluation = RichTextField(blank=True, null=True)
    lien_evaluation = models.URLField(max_length=200)
    fichier_evaluation_pdf = models.FileField(upload_to='file_uploads/evalutions/', blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True, null=True, related_name='evaluations')

    def __str__(self):
        return self.titre_evaluation 
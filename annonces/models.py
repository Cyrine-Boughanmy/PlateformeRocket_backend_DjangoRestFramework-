from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model as user_model
from ckeditor.fields import RichTextField
User = user_model()
class Annonce(models.Model):
    titre_annonce = models.CharField(max_length=45, null=True)
    description_annonce = RichTextField(blank=True, null=True)
    date_annonce = models.DateTimeField(auto_now_add=True)
    publie_par = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='annonces')
    image_annonce = models.ImageField(null=True, upload_to='static/images/annonces/', blank=True)
    fichier_annonce_pdf = models.FileField(upload_to='static/fichiers/annonces/', blank=True)

    def __str__(self):
        return str(self.publie_par) + '|' + self.titre_annonce
    
    class Meta:
        ordering = ['date_annonce']
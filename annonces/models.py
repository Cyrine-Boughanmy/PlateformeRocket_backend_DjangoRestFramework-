from django.db import models
from super_user.models import SuperUser
from django.contrib.auth.models import User

class Annonce(models.Model):
    titre = models.CharField(max_length=45, null=True)
    description = models.TextField(blank=True, default='')
    date_annonce = models.DateTimeField(auto_now_add=True)
    publie_par = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='annonces')
    image_annonce = models.ImageField(null=True, upload_to='static/images/annonces/', blank=True)

    def __str__(self):
        return str(self.publie_par) + '|' + self.titre
    
    class Meta:
        ordering = ['date_annonce']
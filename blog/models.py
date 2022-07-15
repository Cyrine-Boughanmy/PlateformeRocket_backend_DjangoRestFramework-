from django.db import models
# from super_user.models import SuperUser
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

import blog

class Blog(models.Model):
    titre = models.CharField(max_length=45, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='blogs')
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre + '|' + str(self.owner)
    class Meta: 
        ordering = ['date']

class Commentaire(models.Model):
    blog = models.ForeignKey(Blog, related_name="commentaires", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='commentaires')
    body = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['date']

from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model as user_model
from ckeditor.fields import RichTextField
User = user_model()

class Blog(models.Model):
    titre_blog = models.CharField(max_length=45, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='blogs')
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image_Blog = models.ImageField(null=True, upload_to='static/images/blogs/', blank=True)
    ficher_blog = models.FileField(upload_to='file_uploads/blogs/', blank=True)
    # article = models.TextField(blank=True, null=True, max_length=250)

    def __str__(self):
        return self.titre_blog + '|' + str(self.owner)
    class Meta: 
        ordering = ['date']

class Commentaire(models.Model):
    blog = models.ForeignKey(Blog, related_name="commentaires", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='commentaires')
    body = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner) + '|' + str(self.blog)

    class Meta: 
        ordering = ['date']

# Generated by Django 3.1.6 on 2022-08-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_ficher_blog_blog_image_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='article',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
# Generated by Django 3.1.6 on 2022-07-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('exercices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercices',
            name='categorie',
            field=models.ManyToManyField(null=True, to='categories.Categorie'),
        ),
    ]

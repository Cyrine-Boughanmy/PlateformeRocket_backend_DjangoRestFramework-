# Generated by Django 4.0.6 on 2022-07-15 14:01

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('cours', '0005_alter_cours_cours_module'),
        ('exercices', '0002_exercices_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercices',
            name='categorie',
        ),
        migrations.AddField(
            model_name='exercices',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercices', to='categories.categorie'),
        ),
        migrations.RemoveField(
            model_name='exercices',
            name='cours',
        ),
        migrations.AddField(
            model_name='exercices',
            name='cours',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cours', to='cours.cours'),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='enonce',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

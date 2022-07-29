# Generated by Django 3.1.6 on 2022-07-29 12:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0005_alter_cours_cours_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='cours_module',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='ficher_cours',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='titre_module',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='valeur_init',
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_module', models.CharField(max_length=45)),
                ('cours_module', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('valeur_init', models.IntegerField(blank=True, default=25, null=True)),
                ('ficher_cours', models.FileField(blank=True, upload_to='file_uploads/cours/')),
                ('cours', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='cours.cours')),
            ],
        ),
    ]

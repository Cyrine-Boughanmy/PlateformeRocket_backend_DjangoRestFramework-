# Generated by Django 4.0.6 on 2022-07-15 14:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0004_cours_ficher_cours_cours_image_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='cours_module',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.6 on 2022-08-17 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0014_sousmodule_num_module'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cours',
            old_name='description',
            new_name='description_cours',
        ),
        migrations.RenameField(
            model_name='cours',
            old_name='nom',
            new_name='nom_cours',
        ),
        migrations.RenameField(
            model_name='sousmodule',
            old_name='ficher_cours',
            new_name='ficher_cours_pdf',
        ),
    ]

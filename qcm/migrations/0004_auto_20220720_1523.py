# Generated by Django 3.1.6 on 2022-07-20 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qcm', '0003_alter_qcm_options_remove_qcm_option_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='reponse',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='prompt',
            new_name='choix_reponses',
        ),
    ]

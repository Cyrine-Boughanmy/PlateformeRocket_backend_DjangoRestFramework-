# Generated by Django 4.0.6 on 2022-07-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_remove_evaluationclass_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationclass',
            name='enonce',
            field=models.TextField(max_length=100),
        ),
    ]

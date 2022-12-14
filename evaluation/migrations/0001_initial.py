# Generated by Django 3.1.6 on 2022-07-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=45)),
                ('enonce', models.CharField(max_length=100)),
                ('lien', models.CharField(max_length=45)),
                ('fichier_pdf', models.FileField(upload_to='')),
                ('categorie', models.ManyToManyField(null=True, to='categories.Categorie')),
            ],
        ),
    ]

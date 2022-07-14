# Generated by Django 3.1.6 on 2022-07-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qcm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('questions', models.CharField(max_length=200, null=True)),
                ('options_choix', models.CharField(max_length=100, null=True)),
                ('categorie', models.ManyToManyField(null=True, to='categories.Categorie')),
            ],
        ),
    ]

# Generated by Django 3.1.6 on 2022-08-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='image_categorie',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/categories/'),
        ),
    ]

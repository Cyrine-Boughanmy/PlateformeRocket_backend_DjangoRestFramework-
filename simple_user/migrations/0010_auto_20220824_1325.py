# Generated by Django 3.1.6 on 2022-08-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0009_auto_20220818_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=45, null=True, unique=True),
        ),
    ]

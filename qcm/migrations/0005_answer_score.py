# Generated by Django 3.1.6 on 2022-07-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qcm', '0004_auto_20220720_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
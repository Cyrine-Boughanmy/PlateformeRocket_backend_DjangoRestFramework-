# Generated by Django 3.1.6 on 2022-08-01 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0010_auto_20220801_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='sous_module',
        ),
        migrations.AddField(
            model_name='module',
            name='sous_module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sousModules', to='cours.sousmodule'),
        ),
    ]

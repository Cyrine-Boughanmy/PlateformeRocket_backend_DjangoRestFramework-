# Generated by Django 3.1.6 on 2022-08-18 09:50

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0002_auto_20220817_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='user',
            name='avancement',
        ),
        migrations.RemoveField(
            model_name='user',
            name='code_postal',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_de_naissance',
        ),
        migrations.RemoveField(
            model_name='user',
            name='num_tel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='presentation',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ville',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_de_naissance', models.DateField(null=True)),
                ('adresse', models.CharField(max_length=45, null=True)),
                ('code_postal', models.CharField(max_length=45, null=True)),
                ('ville', models.CharField(max_length=45, null=True)),
                ('num_tel', models.CharField(max_length=45, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('resume', models.FileField(blank=True, null=True, upload_to='file_uploads/')),
                ('presentation', models.TextField(blank=True, null=True)),
                ('avancement', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

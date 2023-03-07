# Generated by Django 4.1.6 on 2023-03-01 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(related_name='ptns', to=settings.AUTH_USER_MODEL, verbose_name='participants'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='profile/pictures/avatar.gif', null=True, upload_to='profile/pictures', verbose_name='picture'),
        ),
    ]
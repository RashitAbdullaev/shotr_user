# Generated by Django 4.0.6 on 2022-07-11 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_django_url', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shorturl',
            old_name='user',
            new_name='author',
        ),
    ]

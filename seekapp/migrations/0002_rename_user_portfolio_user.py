# Generated by Django 3.2.9 on 2022-01-25 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seekapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='user',
            new_name='User',
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-05 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='characters',
            new_name='Character',
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-26 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_project_tecnologia_project_cadeira'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tituto',
            new_name='titulo',
        ),
    ]

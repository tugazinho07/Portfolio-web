# Generated by Django 4.0.4 on 2022-05-31 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_project_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='education',
            name='logotipo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='new',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='tecnologia',
            name='logotipo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
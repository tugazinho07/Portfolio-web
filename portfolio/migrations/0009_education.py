# Generated by Django 4.0.4 on 2022-05-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_lab_new_noticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacao', models.CharField(max_length=70)),
                ('curso', models.CharField(max_length=60)),
                ('topicos', models.CharField(default='1', max_length=500)),
                ('local', models.CharField(max_length=50)),
                ('periodo', models.CharField(max_length=50)),
                ('imagem', models.ImageField(default='1', upload_to='static/portfolio/images')),
                ('logotipo', models.ImageField(upload_to='static/portfolio/images')),
            ],
        ),
    ]

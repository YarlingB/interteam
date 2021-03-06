# Generated by Django 2.0.5 on 2018-06-15 15:06

import ckeditor_uploader.fields
import contrapartes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contraparte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('siglas', models.CharField(blank=True, help_text='Siglas o nombre corto de la oganización', max_length=200, null=True, verbose_name='Siglas o nombre corto')),
                ('logo', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=utils.get_file_path)),
                ('fundacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Año de fundación')),
                ('temas', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('generalidades', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('contacto', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=200, null=True)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('rss', models.CharField(blank=True, max_length=200, null=True)),
                ('font_color', contrapartes.models.ColorField(blank=True, max_length=10, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Contrapartes',
            },
        ),
        migrations.CreateModel(
            name='Mensajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('mensaje', ckeditor_uploader.fields.RichTextUploadingField()),
                ('usuario', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('codigo', models.CharField(help_text='Código de 2 letras del país, ejemplo : Nicaragua (ni)', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=utils.get_file_path)),
                ('contraparte', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contrapartes.Contraparte')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contraparte',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contrapartes.Pais'),
        ),
        migrations.AlterUniqueTogether(
            name='contraparte',
            unique_together={('font_color', 'nombre')},
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-15 15:08

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields
import taggit_autosuggest.managers
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name_plural': 'Aportes',
            },
        ),
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True)),
                ('nombre_audio', models.CharField(blank=True, max_length=200, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to=utils.get_file_path)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('tags_aud', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Separar elementos con "," ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Audios',
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('comentario', ckeditor_uploader.fields.RichTextUploadingField()),
                ('aporte', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='foros.Aportes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True)),
                ('nombre_doc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('adjunto', models.FileField(blank=True, null=True, upload_to=utils.get_file_path, verbose_name='Adjunto')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('tags_doc', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Separar elementos con "," ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Foros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('apertura', models.DateField(verbose_name='Apertura y recepción de aportes')),
                ('cierre', models.DateField(verbose_name='Cierre de aportes')),
                ('fecha_skype', models.DateField(verbose_name='Propuesta de reunión skype')),
                ('memoria', models.DateField(verbose_name='Propuesta entrega de memoria')),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contraparte', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Foros',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True)),
                ('nombre_img', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('foto', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=utils.get_file_path, verbose_name='Foto')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('tags_img', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Separar elementos con "," ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Imágenes',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True)),
                ('nombre_video', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('tags_vid', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Separar elementos con "," ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='aportes',
            name='foro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='foros.Foros'),
        ),
        migrations.AddField(
            model_name='aportes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
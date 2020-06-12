# Generated by Django 3.0.7 on 2020-06-11 20:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название статьи')),
                ('auto_slug', models.BooleanField(default=True, verbose_name='Создать ЧПУ ?')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('preview', models.ImageField(null=True, upload_to='promotions/', verbose_name='Картинка превью')),
                ('page_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название страницы SEO')),
                ('page_description', models.TextField(blank=True, null=True, verbose_name='Описание страницы SEO')),
                ('page_keywords', models.TextField(blank=True, null=True, verbose_name='Keywords SEO')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Основной контент')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]

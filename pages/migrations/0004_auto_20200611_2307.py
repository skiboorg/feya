# Generated by Django 3.0.7 on 2020-06-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200611_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leftmenuitem',
            name='icon',
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='name_slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

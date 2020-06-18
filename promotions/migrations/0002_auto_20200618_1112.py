# Generated by Django 2.2.7 on 2020-06-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Отображать ?'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='main_img',
            field=models.ImageField(null=True, upload_to='promotions/', verbose_name='Картинка акции'),
        ),
    ]
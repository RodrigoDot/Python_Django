# Generated by Django 2.0.6 on 2018-07-03 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180703_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(null=True, upload_to='courses/images', verbose_name='Imagen'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180903_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='fotos',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180903_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='fotos',
            field=models.ImageField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]
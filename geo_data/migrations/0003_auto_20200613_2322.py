# Generated by Django 3.0.4 on 2020-06-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_data', '0002_auto_20200321_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='geoobject',
            options={},
        ),
        migrations.AddField(
            model_name='category',
            name='debug',
            field=models.BooleanField(
                default=False,
                verbose_name='Отладочная категория'
            ),
        ),
    ]

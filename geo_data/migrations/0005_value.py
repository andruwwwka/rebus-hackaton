# Generated by Django 2.2.3 on 2019-07-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_data', '0004_auto_20190707_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('infant_school', 'infant_school'), ('school', 'school'), ('bus_station', 'bus_station'), ('hospital', 'hospital'), ('culture', 'culture'), ('sports_ground', 'sports_ground'), ('post_office', 'post_office'), ('waste_points', 'waste_points')], max_length=25)),
                ('first_border', models.FloatField()),
                ('second_border', models.FloatField()),
                ('third_border', models.FloatField()),
            ],
        ),
    ]
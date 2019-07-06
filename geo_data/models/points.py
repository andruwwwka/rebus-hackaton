from django.db import models


class Point(models.Model):
    INFANT_SCHOOL = 'infant_school'
    SCHOOL = 'school'
    BUS_STATION = 'bus_station'
    HOSPITAL = 'hospital'
    CULTURE = 'culture'
    SPORTS_GROUND = 'sports_ground'

    KINDS = [
        (INFANT_SCHOOL, INFANT_SCHOOL),
        (SCHOOL, SCHOOL),
        (BUS_STATION, BUS_STATION),
        (HOSPITAL, HOSPITAL),
        (CULTURE, CULTURE),
        (SPORTS_GROUND, SPORTS_GROUND)
    ]

    lat = models.FloatField()
    lon = models.FloatField()
    title = models.CharField(max_length=256)
    polygon = models.ForeignKey(
        'Polygon',
        on_delete=models.CASCADE,
    )
    kind = models.CharField(
        max_length=25,
        choices=KINDS
    )
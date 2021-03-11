from django.db import models


class Location(models.Model):
    ip = models.CharField(primary_key=True, max_length=15)
    cityId = models.IntegerField(null=True, blank=True)
    cityName = models.CharField(max_length=50, null=True, blank=True)
    regionName = models.CharField(max_length=50, null=True, blank=True)
    districtName = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    country = models.CharField(max_length=20, null=True, blank=True)

from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'cityId',
            'cityName',
            'regionName',
            'districtName',
            'latitude',
            'longitude',
            'country'
        )


class CreateLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('ip',)

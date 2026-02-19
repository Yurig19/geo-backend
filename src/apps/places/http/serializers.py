from rest_framework import serializers


class PlacePointCreateSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class PlacePointResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)
    land_use_description = serializers.CharField(read_only=True)


class LandUseOptionsResponseSerializer(serializers.Serializer):
    land_uses = serializers.ListField(
        child=serializers.CharField(),
        read_only=True,
    )


class LandUseAreaQuerySerializer(serializers.Serializer):
    land_use_description = serializers.CharField(required=True)


class LandUseAreaResponseSerializer(serializers.Serializer):
    land_use_description = serializers.CharField(read_only=True)
    total_area_m2 = serializers.FloatField(read_only=True)

import uuid
from django.contrib.gis.db import models


class PlaceModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    latitude = models.FloatField()
    longitude = models.FloatField()
    land_use_description = models.TextField()

    class Meta:
        db_table = "place"


class LandUseGeometryModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    land_use_geometry = models.TextField(db_index=True)
    geometry = models.GeometryField(srid=4326)

    class Meta:
        db_table = "land_use_geometry"

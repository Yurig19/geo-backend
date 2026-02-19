from decimal import Decimal

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Area, Transform
from django.db.models import Sum

from ..models.place import LandUseGeometryModel, PlaceModel


class PlaceRepository:

    def create_point(
        self, latitude: float, longitude: float, land_use_description: str
    ) -> PlaceModel:
        return PlaceModel.objects.create(
            latitude=latitude,
            longitude=longitude,
            land_use_description=land_use_description,
        )

    def list_points(self) -> list[PlaceModel]:
        return list(PlaceModel.objects.all().order_by("-id"))

    def get_land_use_by_coordinates(
        self, latitude: float, longitude: float
    ) -> str | None:
        point = Point(float(longitude), float(latitude), srid=4326)
        match = (
            LandUseGeometryModel.objects.filter(geometry__intersects=point)
            .only("land_use_geometry")
            .first()
        )
        if not match:
            return None

        return match.land_use_geometry

    def list_land_use_options(self) -> list[str]:
        return list(
            LandUseGeometryModel.objects.values_list("land_use_geometry", flat=True)
            .distinct()
            .order_by("land_use_geometry")
        )

    def get_total_area_by_land_use(self, land_use_geometry: str) -> Decimal:
        result = (
            LandUseGeometryModel.objects.filter(land_use_geometry=land_use_geometry)
            .annotate(area_m2=Area(Transform("geometry", 3857)))
            .aggregate(total_area=Sum("area_m2"))
        )
        total_area = result["total_area"]
        if not total_area:
            return Decimal("0")

        if hasattr(total_area, "sq_m"):
            return Decimal(str(total_area.sq_m))

        return Decimal(str(total_area))

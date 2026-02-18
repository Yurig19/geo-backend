from .models import PlaceModel
from ..domain.entities import Place


class PlaceRepository:

    def exists_by_name(self, name: str) -> bool:
        return PlaceModel.objects.filter(name=name).exists()

    def create(self, place: Place) -> PlaceModel:
        return PlaceModel.objects.create(
            name=place.name,
            latitude=place.latitude,
            longitude=place.longitude,
        )

from ...application.dtos.place_point_response_dto import PlacePointResponseDTO
from ...infrastructure.repositories.place_repository import PlaceRepository


class ListPlacePointsUseCase:

    def execute(self) -> list[PlacePointResponseDTO]:
        repository = PlaceRepository()
        points = repository.list_points()

        return [
            PlacePointResponseDTO(
                id=point.id,
                latitude=point.latitude,
                longitude=point.longitude,
                land_use_description=point.land_use_description,
            )
            for point in points
        ]

from src.core.error_code.place import PlaceErrorCode
from src.core.exceptions import DomainException

from ...application.dtos.create_place_point_dto import CreatePlacePointDTO
from ...application.dtos.place_point_response_dto import PlacePointResponseDTO
from ...infrastructure.repositories.place_repository import PlaceRepository


class CreatePlacePointUseCase:

    def execute(self, data: CreatePlacePointDTO) -> PlacePointResponseDTO:
        repository = PlaceRepository()

        if not (-90 <= data.latitude <= 90) or not (-180 <= data.longitude <= 180):
            raise DomainException(
                message="Latitude/longitude inválidos",
                code=PlaceErrorCode.INVALID_COORDINATES,
            )

        land_use_description = repository.get_land_use_by_coordinates(
            latitude=data.latitude,
            longitude=data.longitude,
        )
        if not land_use_description:
            raise DomainException(
                message="Nenhum uso do solo encontrado para o ponto informado",
                code=PlaceErrorCode.NOT_FOUND,
            )

        point = repository.create_point(
            latitude=data.latitude,
            longitude=data.longitude,
            land_use_description=land_use_description,
        )

        return PlacePointResponseDTO(
            id=point.id,
            latitude=point.latitude,
            longitude=point.longitude,
            land_use_description=point.land_use_description,
        )

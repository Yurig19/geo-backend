from src.core.error_code.place import PlaceErrorCode
from ...domain.entities import Place
from ...infrastructure.repositories import PlaceRepository
from ...application.dtos.place_response_dto import PlaceResponseDTO
from ...application.dtos.create_place_dto import CreatePlaceDTO

from src.core.exceptions import DomainException


class CreatePlaceUseCase:

    def execute(self, data: CreatePlaceDTO) -> PlaceResponseDTO:
        repository = PlaceRepository()

        if repository.exists_by_name(data.name):
            raise DomainException(
                message="Já existe um local com esse nome",
                code=PlaceErrorCode.ALREADY_EXISTS,
            )

        place = Place(
            name=data.name,
            latitude=data.latitude,
            longitude=data.longitude,
        )

        created = repository.create(place)

        return PlaceResponseDTO(
            id=created.id,
            name=created.name,
            latitude=created.latitude,
            longitude=created.longitude,
        )

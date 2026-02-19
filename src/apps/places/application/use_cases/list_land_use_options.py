from ...application.dtos.land_use_options_response_dto import LandUseOptionsResponseDTO
from ...infrastructure.repositories.place_repository import PlaceRepository


class ListLandUseOptionsUseCase:

    def execute(self) -> LandUseOptionsResponseDTO:
        repository = PlaceRepository()
        land_uses = repository.list_land_use_options()
        return LandUseOptionsResponseDTO(land_uses=land_uses)

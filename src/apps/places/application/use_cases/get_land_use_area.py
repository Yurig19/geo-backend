from ...application.dtos.land_use_area_query_dto import LandUseAreaQueryDTO
from ...application.dtos.land_use_area_response_dto import LandUseAreaResponseDTO
from ...infrastructure.repositories.place_repository import PlaceRepository


class GetLandUseAreaUseCase:

    def execute(self, data: LandUseAreaQueryDTO) -> LandUseAreaResponseDTO:
        repository = PlaceRepository()
        total_area_m2 = repository.get_total_area_by_land_use(data.land_use_description)

        return LandUseAreaResponseDTO(
            land_use_description=data.land_use_description,
            total_area_m2=float(total_area_m2),
        )

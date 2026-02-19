from dataclasses import dataclass


@dataclass
class LandUseAreaResponseDTO:
    land_use_description: str
    total_area_m2: float

from dataclasses import dataclass


@dataclass
class LandUseOptionsResponseDTO:
    land_uses: list[str]

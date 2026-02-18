from dataclasses import dataclass


@dataclass
class PlaceResponseDTO:
    id: int
    name: str
    latitude: float
    longitude: float

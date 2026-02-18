from dataclasses import dataclass


@dataclass
class CreatePlaceDTO:
    name: str
    latitude: float
    longitude: float

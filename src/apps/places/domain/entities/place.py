from dataclasses import dataclass
from uuid import UUID


@dataclass
class Place:
    id: UUID
    latitude: float
    longitude: float
    land_use_description: str

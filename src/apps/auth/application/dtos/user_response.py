from dataclasses import dataclass


@dataclass
class UserResponseDTO:
    id: int
    username: str
    email: str

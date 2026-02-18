from dataclasses import dataclass
from .user_response import UserResponseDTO


@dataclass
class RegisterResponseDTO:
    user: UserResponseDTO

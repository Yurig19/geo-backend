from dataclasses import dataclass
from .user_response import UserResponseDTO


@dataclass(frozen=True)
class LoginResponseDTO:
    access: str
    refresh: str
    user: UserResponseDTO

    def to_dict(self) -> dict:
        return {
            "access": self.access,
            "refresh": self.refresh,
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "email": self.user.email,
            },
        }

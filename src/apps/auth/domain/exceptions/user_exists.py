from src.core.exceptions import DomainException
from src.core.error_code.auth import AuthErrorCode


class UserAlreadyExistsException(DomainException):
    def __init__(self):
        super().__init__(
            message="Usuário já existe",
            code=AuthErrorCode.USERNAME_ALREADY_EXISTS,
        )

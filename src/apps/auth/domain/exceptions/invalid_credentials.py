from src.core.exceptions import DomainException
from src.core.error_code.auth import AuthErrorCode


class InvalidCredentialsException(DomainException):
    def __init__(self):
        super().__init__(
            message="Usuário ou senha inválidos",
            code=AuthErrorCode.INVALID_CREDENTIALS,
        )

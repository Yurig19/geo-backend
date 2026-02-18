from src.core.error_code.base import AppErrorCode


class DomainException(Exception):
    def __init__(
        self,
        message: str,
        code: AppErrorCode,
    ):
        self.message = message
        self.code = code.value
        self.status_code = code.status
        super().__init__(message)

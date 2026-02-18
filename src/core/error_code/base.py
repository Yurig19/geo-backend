from enum import Enum
from http import HTTPStatus


class AppErrorCode(str, Enum):
    def __new__(cls, code: str, http_status: HTTPStatus):
        obj = str.__new__(cls, code)
        obj._value_ = code
        obj.http_status = http_status
        return obj

    @property
    def status(self) -> int:
        return self.http_status.value


class BaseErrorCode(AppErrorCode):
    VALIDATION_ERROR = ("VALIDATION_ERROR", HTTPStatus.BAD_REQUEST)
    INTERNAL_ERROR = ("INTERNAL_ERROR", HTTPStatus.INTERNAL_SERVER_ERROR)
    NOT_FOUND = ("NOT_FOUND", HTTPStatus.NOT_FOUND)
    UNAUTHORIZED = ("UNAUTHORIZED", HTTPStatus.UNAUTHORIZED)
    FORBIDDEN = ("FORBIDDEN", HTTPStatus.FORBIDDEN)

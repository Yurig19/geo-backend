from http import HTTPStatus
from .base import AppErrorCode


class PlaceErrorCode(AppErrorCode):
    ALREADY_EXISTS = ("PLACE_ALREADY_EXISTS", HTTPStatus.CONFLICT)
    NOT_FOUND = ("PLACE_NOT_FOUND", HTTPStatus.NOT_FOUND)
    INVALID_COORDINATES = ("PLACE_INVALID_COORDINATES", HTTPStatus.BAD_REQUEST)

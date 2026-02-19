import logging
from typing import Any

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from .exceptions import DomainException


logger = logging.getLogger(__name__)


def custom_exception_handler(
    exc: Exception,
    context: dict[str, Any],
) -> Response:
    response = exception_handler(exc, context)

    if isinstance(exc, DomainException):
        return Response(
            {
                "error": True,
                "code": exc.code,
                "message": exc.message,
            },
            status=exc.status_code,
        )

    if response is not None:
        return Response(
            {
                "error": True,
                "code": "VALIDATION_ERROR",
                "message": "Erro na requisição",
                "details": response.data,
            },
            status=response.status_code,
        )

    logger.exception("Erro inesperado na aplicação")

    return Response(
        {
            "error": True,
            "code": "INTERNAL_ERROR",
            "message": "Erro interno no servidor",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

from fastapi import Request
from fastapi.responses import JSONResponse

from src.infrastructure.logging.logger import logger

from src.shared.exceptions.custom_exceptions import (BusinessException)

from fastapi.exceptions import RequestValidationError


async def business_exception_handler(
    request: Request,
    exc: BusinessException
):

    logger.warning(
        f"{request.method} "
        f"{request.url.path} "
        f"{exc.message}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "Success": False,
            "Message": exc.message,
            "Status": exc.status_code
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(exc)

    return JSONResponse(
        status_code=500,
        content={
            "Success": False,
            "Message": "Error interno del servidor",
            "Status": 500
        }
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    return JSONResponse(
        status_code=422,
        content={
            "Success": False,
            "Message": "Error de validación",
            "Status": 422,
            "Errors": exc.errors()
        }
    )
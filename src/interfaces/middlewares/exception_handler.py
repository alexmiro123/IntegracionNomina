from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.shared.exceptions.custom_exceptions import BusinessException
from src.shared.responses.api_response import ApiResponse


async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            Success=False,
            Message=str(exc.message),
            Status=exc.status_code,
            Data=None
        ).model_dump()
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            Success=False,
            Message=str(exc.detail),
            Status=exc.status_code,
            Data=None
        ).model_dump()
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=ApiResponse(
            Success=False,
            Message="Error de validación",
            Status=422,
            Data=exc.errors()
        ).model_dump()
    )
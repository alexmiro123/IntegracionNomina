from fastapi import FastAPI

from src.shared.config.settings import settings
from src.interfaces.api.health_controller import (router as health_router)
from src.interfaces.api.auth_controller import (router as auth_router)
from src.interfaces.middlewares.request_middleware import (RequestMiddleware)

from src.shared.exceptions.global_handler import (
    business_exception_handler,
    generic_exception_handler
)

from src.shared.exceptions.custom_exceptions import (
    BusinessException
)

from fastapi.exceptions import RequestValidationError
from src.shared.exceptions.global_handler import (
    validation_exception_handler
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(
    RequestMiddleware
)

app.add_exception_handler(
    BusinessException,
    business_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(
    health_router
)

app.include_router(
    auth_router
)


app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)
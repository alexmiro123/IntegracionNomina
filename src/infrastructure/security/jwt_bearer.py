from fastapi import Request
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from src.shared.exceptions.custom_exceptions import (
    BusinessException
)

from src.infrastructure.security.jwt_service import (
    verify_token
)


class JWTBearer(
    HTTPBearer
):

    def __init__(self,required_scopes: list[str] | None = None):
        
        super().__init__(auto_error=False)

        self.required_scopes = (
            required_scopes or []
        )

    async def __call__(
            self,
            request: Request
    ):

        credentials: HTTPAuthorizationCredentials = (
            await super().__call__(
                request
            )
        )

        if not credentials:

            raise BusinessException(
                "Token requerido",
                401
            )

        if credentials.scheme.lower() != "bearer":

            raise BusinessException(
                "Esquema inválido",
                401
            )

        payload = verify_token(
            credentials.credentials
        )

        if not payload:

            raise BusinessException(
                "Token inválido",
                401
            )

        token_scopes = payload.get(
            "scope",
            []
        )
        for scope in self.required_scopes:

            if scope not in token_scopes:

                raise BusinessException(
                    f"Scope requerido: {scope}",
                    403
                )

        request.state.user = payload

        return payload
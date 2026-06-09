from fastapi import Request

from src.shared.exceptions.custom_exceptions import (
    BusinessException
)


class ScopeValidator:

    def __init__(
            self,
            required_scope: str
    ):
        self.required_scope = required_scope

    async def __call__(
            self,
            request: Request
    ):

        payload = request.state.user

        scopes = payload.get(
            "scope",
            []
        )

        if self.required_scope not in scopes:

            raise BusinessException(
                "No tiene permisos",
                403
            )

        return True
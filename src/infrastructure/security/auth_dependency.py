from fastapi import Depends
from fastapi import Header

from shared.exceptions.global_handler import (
    UnauthorizedException
)

from infrastructure.security.jwt_service import (
    verify_token
)


def jwt_required(
        authorization: str = Header(None)
):

    if not authorization:
        raise UnauthorizedException(
            "Token requerido"
        )

    if not authorization.startswith(
            "Bearer "
    ):
        raise UnauthorizedException(
            "Formato inválido"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = verify_token(token)

    if payload is None:
        raise UnauthorizedException(
            "Token inválido"
        )

    return payload
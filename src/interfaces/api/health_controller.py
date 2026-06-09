from fastapi import APIRouter

from src.infrastructure.database.oracle import (test_connection)

from src.infrastructure.security.jwt_service import (
    create_access_token,
    verify_token
)

from src.infrastructure.security.jwt_bearer import (
    JWTBearer
)
from fastapi import Depends

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("")
async def health():

    return {
        "success": True,
        "message": "API funcionando"
    }

@router.get("/db")
async def health_db():

    test_connection()

    return {
        "success": True,
        "message": "Oracle conectado"
    }


@router.get("/token")
async def token_test():

    token = create_access_token(
        {
            "sub": "nomina_provider",
            "client_id": "nomina_provider",
            "scope": [
                "employees:create",
                "employees:update"
            ]
        }
    )

    return {
        "token": token
    }


@router.get("/token/verify")
async def verify_token_test():

    token = create_access_token(
        {
            "sub": "nomina_provider",
            "client_id": "nomina_provider",
            "scope": [
                "employees:create",
                "employees:update"
            ]
        }
    )

    payload = verify_token(
        token
    )

    return payload



router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("")
async def get_employees(
    payload=Depends(
        JWTBearer(
            ["employees:read"]
        )
    )
):

    return {
        "message": "Consulta empleados",
        "payload": payload
    }
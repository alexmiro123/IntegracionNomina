from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import jwt
from jose import JWTError
from src.shared.exceptions.custom_exceptions import (
    BusinessException
)

from src.shared.config.settings import settings


def _read_private_key():

    with open(
            settings.PRIVATE_KEY,
            "r",
            encoding="utf-8"
    ) as file:

        return file.read()
    

def _read_public_key():

    with open(
            settings.PUBLIC_KEY,
            "r",
            encoding="utf-8"
    ) as file:

        return file.read()    
    


def create_access_token(
        payload: dict
) -> str:

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=settings.JWT_EXPIRE_MINUTES
    )

    data = payload.copy()

    data.update(
        {
            "exp": expire,
            "iat": datetime.now(timezone.utc),
            "iss": settings.APP_NAME
        }
    )

    token = jwt.encode(
        data,
        _read_private_key(),
        algorithm=settings.JWT_ALGORITHM
    )

    return token    



def verify_token(
        token: str
) -> dict:

    try:

        payload = jwt.decode(
            token,
            _read_public_key(),
            algorithms=[
                settings.JWT_ALGORITHM
            ]
        )

        return payload

    except JWTError:

        raise BusinessException(
            message="Token inválido o expirado",
            status_code=401
        )
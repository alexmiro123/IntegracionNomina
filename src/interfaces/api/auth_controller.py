from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from src.infrastructure.database.dependencies import (get_db)
from src.infrastructure.persistence.repositories.oracle_provider_repository import (OracleProviderRepository)
from src.application.use_cases.auth.generate_token_use_case import (GenerateTokenUseCase)
from src.application.dtos.auth.token_request import (TokenRequest)
from src.shared.config.settings import settings

router = APIRouter(
    prefix="/oauth",
    tags=["OAuth"]
)


@router.post("/token")
async def token(request: TokenRequest,db: Session = Depends(get_db)):

    repository = (OracleProviderRepository(db))

    use_case = (GenerateTokenUseCase(repository))

    access_token = use_case.execute(
        request.provider_id,
        request.provider_secret
    )

    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": settings.JWT_EXPIRE_MINUTES 
    }
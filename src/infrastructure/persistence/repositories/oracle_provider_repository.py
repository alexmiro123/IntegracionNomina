from sqlalchemy.orm import Session

from src.domain.auth.entities.provider_entity import (
    ProviderEntity
)

from src.domain.auth.repositories.provider_repository import (
    ProviderRepository
)

from src.infrastructure.models.external_provider_model import (
    ExternalProviderModel
)


class OracleProviderRepository(
    ProviderRepository
):

    def __init__(self,db: Session):
        self.db = db

    def get_by_provider_id(self,provider_id: str):

        result = (
            self.db.query(
                ExternalProviderModel
            )
            .filter(
                ExternalProviderModel.PROVIDER_ID
                == provider_id
            )
            .first()
        )

        if not result:
            return None

        return ProviderEntity(
            provider_id=result.PROVIDER_ID,
            provider_secret_hash=result.PROVIDER_SECRET_HASH,
            provider_name=result.PROVIDER_NAME,
            status=result.STATUS,
            provider_scopes=(
                result.PROVIDER_SCOPES.split(",")
                if result.PROVIDER_SCOPES
                else []
            )
        )
from src.shared.exceptions.custom_exceptions import (
    BusinessException
)

from src.infrastructure.security.password_service import (verify_password)
from src.infrastructure.security.jwt_service import (create_access_token)
from src.shared.utils.scope_utils import (parse_scopes)



class GenerateTokenUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        provider_id: str,
        provider_secret: str
    ):

        provider = (
            self.repository
            .get_by_provider_id(
                provider_id
            )
        )

        if not provider:

            raise BusinessException(
                "Proveedor inválido",
                401
            )

        if not provider.status:

            raise BusinessException(
                "Proveedor inactivo",
                401
            )

        if not verify_password(
            provider_secret,
            provider.provider_secret_hash
        ):

            raise BusinessException(
                "Credenciales inválidas",
                401
            )

        scopes = provider.provider_scopes

        token = create_access_token(
            {
                "sub": provider.provider_id,
                "client_id": provider.provider_id,
                "scope": scopes
            }
        )

        return token
from abc import ABC
from abc import abstractmethod

from src.domain.auth.entities.provider_entity import (
    ProviderEntity
)


class ProviderRepository(ABC):

    @abstractmethod
    def get_by_provider_id(
        self,
        provider_id: str
    ) -> ProviderEntity | None:
        pass
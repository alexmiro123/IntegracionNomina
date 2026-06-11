from abc import ABC
from abc import abstractmethod


from abc import ABC
from abc import abstractmethod


class CatalogRepository(ABC):

    @abstractmethod
    def exists(
        self,
        model,
        empresa_field,
        codigo_field,
        empresa,
        codigo
    ) -> bool:
        pass
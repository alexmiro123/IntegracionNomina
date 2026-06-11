from sqlalchemy.orm import Session

from src.shared.constants.catalog_constants import (
    CATALOGS
)



class OracleCatalogRepository:

    def __init__(self, db: Session):
        self.db = db

    def exists_catalog(
        self,
        catalog_name: str,
        empresa: int,
        codigo: int
    ) -> bool:

        model, empresa_field, codigo_field = (
            CATALOGS[catalog_name]
        )

        return (
            self.db.query(model)
            .filter(
                empresa_field == empresa,
                codigo_field == codigo
            )
            .first()
            is not None
        )


from sqlalchemy import (
    Column,
    Integer,
    String
)
from src.infrastructure.database.base import Base

class AlmacenModel(Base):

    __tablename__ = "ALMACEN"

    ALM_EMPRESA = Column(
        Integer,
        primary_key=True
    )

    ALM_CODIGO = Column(
        Integer,
        primary_key=True
    )

    ALM_NOMBRE = Column(
        String(100)
    )

    ALM_ID = Column(
        String(10)
    )
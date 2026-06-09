from sqlalchemy import (
    Column,
    String,
    Integer,
    Date
)

from src.infrastructure.database.base import Base


class ExternalProviderModel(Base):

    __tablename__ = "EXTERNAL_PROVIDER"

    PROVIDER_ID = Column(
        String(100),
        primary_key=True
    )

    PROVIDER_SECRET_HASH = Column(
        String(500),
        nullable=False
    )

    PROVIDER_NAME = Column(
        String(200)
    )

    STATUS = Column(
        Integer
    )

    CREATED_AT = Column(
        Date
    )

    PROVIDER_SCOPES = Column(
        String(1000)
    )
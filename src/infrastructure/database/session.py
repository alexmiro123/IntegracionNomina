from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.oracle import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
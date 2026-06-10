from sqlalchemy import create_engine
from sqlalchemy import text

from src.shared.config.settings import settings

import oracledb

oracledb.init_oracle_client(
    lib_dir=settings.ORACLE_CLIENT_PATH
)

DATABASE_URL = (
    f"oracle+oracledb://"
    f"{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/?"
    f"service_name={settings.DB_SERVICE}"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=30,
    pool_timeout=30,
    pool_pre_ping=True,
    pool_recycle=3600
)

def test_connection():

    with engine.connect() as conn:

        conn.execute(
            text("SELECT 1 FROM DUAL")
        )

        return True
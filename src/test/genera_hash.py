from src.infrastructure.security.password_service import (
    hash_password
)

print(
    hash_password(
        "123"
    )
)
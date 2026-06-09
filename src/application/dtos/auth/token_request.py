from pydantic import BaseModel


class TokenRequest(
    BaseModel
):

    provider_id: str

    provider_secret: str
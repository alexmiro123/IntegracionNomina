from dataclasses import dataclass


@dataclass
class ProviderEntity:

    provider_id: str

    provider_secret_hash: str

    provider_name: str

    status: bool

    provider_scopes: str
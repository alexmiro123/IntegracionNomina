def parse_scopes(
        scopes: str
) -> list[str]:

    if not scopes:
        return []

    return [
        scope.strip().strip("'").strip('"')
        for scope in scopes.split(",")
        if scope.strip()
    ]
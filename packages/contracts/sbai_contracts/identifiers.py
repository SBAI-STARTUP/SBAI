from uuid import UUID


def is_valid_request_id(value: str | None) -> bool:
    if not value:
        return False

    try:
        UUID(value)
    except (ValueError, AttributeError, TypeError):
        return False

    return True

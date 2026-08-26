from typing import Any


class SBAIError(Exception):
    def __init__(
        self,
        error: str,
        message: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        self.error = error
        self.message = message
        self.details = details

        super().__init__(message)

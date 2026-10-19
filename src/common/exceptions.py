class ApplicationError(Exception):
    def __init__(self, status_code: int, code: str, message: str) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message
        super().__init__(message)


class UserNotFoundError(ApplicationError):
    def __init__(self, user_id: int) -> None:
        super().__init__(404, "user_not_found", f"User {user_id} was not found.")


class UserConflictError(ApplicationError):
    def __init__(self) -> None:
        super().__init__(
            409,
            "user_conflict",
            "A user with that name or email already exists.",
        )
# template.py

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DIRECTORIES = [
    # API versioning
    "src/api/v1",

    # Feature modules
    "src/auth",
    "src/users",
    "src/places",
    "src/bookings",

    # Shared modules
    "src/common",
    "src/security",
    "src/errors",

    # Database migrations
    "migrations",

    # Tests
    "tests/unit",
    "tests/integration",

    # Project support
    "scripts",
]

FILES = [
    # Root files
    "main.py",
    ".env",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    "Dockerfile",

    # Application entry point and configuration
    "src/__init__.py",
    "src/main.py",
    "src/config.py",
    "src/database.py",
    "src/dependencies.py",

    # API registration and versioning
    "src/api/__init__.py",
    "src/api/v1/__init__.py",
    "src/api/v1/router.py",

    # Authentication
    "src/auth/__init__.py",
    "src/auth/routes.py",
    "src/auth/controller.py",
    "src/auth/service.py",
    "src/auth/repository.py",
    "src/auth/schemas.py",

    # Users
    "src/users/__init__.py",
    "src/users/routes.py",
    "src/users/controller.py",
    "src/users/service.py",
    "src/users/repository.py",
    "src/users/schemas.py",
    "src/users/models.py",

    # Places / workspaces
    "src/places/__init__.py",
    "src/places/routes.py",
    "src/places/controller.py",
    "src/places/service.py",
    "src/places/repository.py",
    "src/places/schemas.py",
    "src/places/models.py",

    # Bookings
    "src/bookings/__init__.py",
    "src/bookings/routes.py",
    "src/bookings/controller.py",
    "src/bookings/service.py",
    "src/bookings/repository.py",
    "src/bookings/schemas.py",
    "src/bookings/models.py",

    # Shared components
    "src/common/__init__.py",
    "src/common/responses.py",
    "src/common/pagination.py",
    "src/common/exceptions.py",

    # Security
    "src/security/__init__.py",
    "src/security/jwt.py",
    "src/security/passwords.py",
    "src/security/permissions.py",

    # Centralized error handling
    "src/errors/__init__.py",
    "src/errors/handlers.py",

    # Tests
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
]


def create_structure() -> None:
    for directory in DIRECTORIES:
        path = PROJECT_ROOT / directory
        path.mkdir(parents=True, exist_ok=True)

    for filename in FILES:
        path = PROJECT_ROOT / filename
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            print(f"Skipped existing file: {filename}")
            continue

        path.touch()
        print(f"Created file: {filename}")

    print("\\nProject structure created successfully.")


if __name__ == "__main__":
    create_structure()

# template.py

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DIRECTORIES = [
    # API versioning
    "src/api/v1",

    # Feature modules
    "src/auth",
    "src/users",

    # Shared modules
    "src/common",
    "src/security",
    "src/errors",

    # Project support
    "migrations",
    "tests/unit",
    "tests/integration",
    "scripts",
]

FILES = [
    # Root files
    "app.py",
    ".env.example",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    "Dockerfile",

    # Application factory and configuration
    "src/__init__.py",
    "src/config.py",
    "src/extensions.py",

    # API registration and versioning
    "src/api/__init__.py",
    "src/api/v1/__init__.py",
    "src/api/v1/routes.py",

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

    print("\nProject structure created successfully.")


if __name__ == "__main__":
    create_structure()

from sqlalchemy.orm import Session

from src.common.exceptions import UserNotFoundError
from src.users.models import User
from src.users.repository import UserRepository
from src.users.schemas import UserInput


def create_user(db: Session, user_data: UserInput) -> User:
    return UserRepository(db).create(user_data)


def list_users(db: Session) -> list[User]:
    return UserRepository(db).list()


def get_user(db: Session, user_id: int) -> User:
    user = UserRepository(db).get(user_id)
    if user is None:
        raise UserNotFoundError(user_id)
    return user


def update_user(db: Session, user_id: int, user_data: UserInput) -> User:
    user = get_user(db, user_id)
    return UserRepository(db).update(user, user_data)


def delete_user(db: Session, user_id: int) -> None:
    user = get_user(db, user_id)
    UserRepository(db).delete(user)
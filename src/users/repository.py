from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.common.exceptions import UserConflictError
from src.users.models import User
from src.users.schemas import UserInput


class UserRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def create(self, user_data: UserInput) -> User:
        user = User(username=user_data.userName, email=user_data.userEmail)
        self._db.add(user)
        try:
            self._db.commit()
        except IntegrityError as exc:
            self._db.rollback()
            raise UserConflictError() from exc
        self._db.refresh(user)
        return user

    def list(self) -> list[User]:
        statement = select(User).order_by(User.id)
        return list(self._db.scalars(statement).all())

    def get(self, user_id: int) -> User | None:
        return self._db.get(User, user_id)

    def update(self, user: User, user_data: UserInput) -> User:
        user.username = user_data.userName
        user.email = user_data.userEmail
        try:
            self._db.commit()
        except IntegrityError as exc:
            self._db.rollback()
            raise UserConflictError() from exc
        self._db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self._db.delete(user)
        self._db.commit()

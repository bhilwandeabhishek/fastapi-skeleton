from fastapi import APIRouter
from fastapi import Depends, Response, status
from sqlalchemy.orm import Session

from src.common.responses import ERROR_RESPONSES
from src.database import get_db
from src.users import service
from src.users.models import User
from src.users.schemas import UserInput, UserRead

router = APIRouter()


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    responses=ERROR_RESPONSES,
)
def create_user(user_data: UserInput, db: Session = Depends(get_db)) -> User:
    return service.create_user(db, user_data)


@router.get(
    "/",
    response_model=list[UserRead],
    tags=["Users"],
    responses=ERROR_RESPONSES,
)
def list_users(db: Session = Depends(get_db)) -> list[User]:
    return service.list_users(db)


@router.get(
    "/{user_id}",
    response_model=UserRead,
    tags=["Users"],
    responses=ERROR_RESPONSES,
)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    return service.get_user(db, user_id)


@router.put(
    "/{user_id}",   
    response_model=UserRead,
    tags=["Users"],
    responses=ERROR_RESPONSES,
)
def update_user(
    user_id: int,
    user_data: UserInput,
    db: Session = Depends(get_db),
) -> User:
    return service.update_user(db, user_id, user_data)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Users"],
    responses=ERROR_RESPONSES,
)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> Response:
    service.delete_user(db, user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
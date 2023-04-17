from typing import Any, Literal, Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from src import models
from src.constants import IS_DEV
from src.database import get_db
from src.schemas.user import UserIn, UserOut
from src.store.datastore import DataStore

SortOrder = Literal["asc", "desc"]

router = APIRouter(tags=["Item"], prefix="/item")

USERS_TO_WRITE_TO_DB = [
    {"name": "foo", "number": 1337, "is_happy": True},
    {"name": "bar", "number": 42069, "is_happy": False},
]
USER_TO_WRITE_TO_DB = {"name": "foo", "number": 1337, "is_happy": True}
USER_TO_UPDATE = {"name": "hello", "number": 1337, "is_happy": True}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: UserIn, db: Session = Depends(get_db)):
    DataStore(db).create(models.User(**request.dict()))
    return "success"


@router.post("/many", status_code=status.HTTP_201_CREATED)
def create_many(request: list[UserIn], db: Session = Depends(get_db)):
    DataStore(db).create_many([models.User(**data.dict()) for data in request])
    return "success"


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get(
    name: Optional[str] = None,
    number: Optional[int] = None,
    db: Session = Depends(get_db),
):
    return DataStore(db).get(models.User, filter={"name": name, "number": number})


@router.get("/all", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_all(db: Session = Depends(get_db)):
    return DataStore(db).get_all(models.User)


@router.get("/search", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def search(
    field: str,
    q: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort_col: Optional[str] = None,
    sort: Optional[SortOrder] = None,
    db: Session = Depends(get_db),
):
    return DataStore(db).search(models.User, field, q, limit, offset, sort_col, sort)


@router.put("/", status_code=status.HTTP_201_CREATED)
def update(filter: dict = {"id": 12}, db: Session = Depends(get_db)):
    return DataStore(db).update(filter, models.User, USER_TO_UPDATE)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str, name: str, number: str, db: Session = Depends(get_db)):
    return DataStore(db).delete(
        models.User, filter={"id": id, "name": name, "number": number}
    )

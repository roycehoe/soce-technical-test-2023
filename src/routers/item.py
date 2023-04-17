from typing import Any, Literal, Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from src import models
from src.constants import IS_DEV
from src.database import get_db
from src.schemas.item import ItemIn, ItemOut
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
def create(request: ItemIn, db: Session = Depends(get_db)):
    DataStore(db).create(models.Item(**request.dict()))
    return {
        "message": "Item created"
    }  # TODO: Create raising of errors for proper handling


@router.post("/many", status_code=status.HTTP_201_CREATED)
def create_many(request: list[ItemIn], db: Session = Depends(get_db)):
    DataStore(db).create_many([models.Item(**data.dict()) for data in request])
    return {
        "message": "Items created"
    }  # TODO: Create raising of errors for proper handling


@router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=list[ItemOut])
def get(
    item_id: int,
    db: Session = Depends(get_db),
):
    if item := DataStore(db).get(models.Item, filter={"id": item_id}):
        return item
    return {
        "message": "No items found"
    }  # TODO: Create raising of errors for proper handling


@router.get("/all/", status_code=status.HTTP_200_OK, response_model=list[ItemOut])
def get_all(db: Session = Depends(get_db)):
    if all_items := DataStore(db).get_all(models.Item):
        return all_items
    return {
        "message": "No items found"
    }  # TODO: Create raising of errors for proper handling


@router.get("/search", status_code=status.HTTP_200_OK, response_model=list[ItemOut])
def search(
    field: str,
    q: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort_col: Optional[str] = None,
    sort: Optional[SortOrder] = None,
    db: Session = Depends(get_db),
):
    if searched_items := DataStore(db).search(
        models.Item, field, q, limit, offset, sort_col, sort
    ):
        return searched_items
    return {
        "message": "No items found"
    }  # TODO: Create raising of errors for proper handling


@router.put("/{item_id}", status_code=status.HTTP_201_CREATED)
def update(item_id: int, updated_item: ItemIn, db: Session = Depends(get_db)):
    return DataStore(db).update({"id": item_id}, models.Item, updated_item)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str, db: Session = Depends(get_db)):
    return DataStore(db).delete(models.Item, filter={"id": id})

from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from sqlalchemy.orm import Session

from src import models
from src.constants import PREPOPULATED_ITEMS
from src.database import get_db
from src.schemas.item import ItemIn, ItemOut
from src.store.datastore import DataStore

SortOrder = Literal["asc", "desc"]

router = APIRouter(tags=["Items"], prefix="/items")


@router.on_event("startup")
def prepopulate_db(prepopulated_items: list[dict] = PREPOPULATED_ITEMS):
    logger.info("prepopulating database with mock data")
    db = next(get_db())
    items = [models.Item(**data) for data in prepopulated_items]
    DataStore(db).create_many(items)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_many(request: list[ItemIn], db: Session = Depends(get_db)):
    DataStore(db).create_many([models.Item(**data.dict()) for data in request])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ItemOut])
def get_all(db: Session = Depends(get_db)):
    if all_items := DataStore(db).get_all(models.Item):
        return all_items
    raise HTTPException(status_code=404, detail=f"No items in database found")


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
    raise HTTPException(
        status_code=404, detail=f"No items for given search parameters found"
    )

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from sqlalchemy.orm import Session

from src import models
from src.database import get_db
from src.schemas.item import ItemIn, ItemOut
from src.store.datastore import DataStore

router = APIRouter(tags=["Item"], prefix="/item")


@router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=ItemOut)
def get(
    item_id: int,
    db: Session = Depends(get_db),
):
    if item := DataStore(db).get(models.Item, item_id):
        return item
    raise HTTPException(
        status_code=404, detail=f"Item with item_id: {item_id} not found"
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: ItemIn, db: Session = Depends(get_db)):
    if created_item := DataStore(db).create(models.Item(**request.dict())):
        return created_item
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=f"Failed to create item: {request}",
    )


@router.put("/{item_id}", status_code=status.HTTP_201_CREATED)
def update(item_id: int, updated_item: ItemIn, db: Session = Depends(get_db)):
    try:
        DataStore(db).update(item_id, models.Item, updated_item.dict())
        return
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item of item_id {item_id} not found",
        )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    try:
        DataStore(db).delete(models.Item, item_id)
        return

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item of item_id {item_id} not found",
        )

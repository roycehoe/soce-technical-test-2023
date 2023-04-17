from fastapi import APIRouter, Depends, HTTPException, status
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
        detail=f"Faied to create item: {request}",
    )


@router.put("/{item_id}", status_code=status.HTTP_201_CREATED)
def update(item_id: int, updated_item: ItemIn, db: Session = Depends(get_db)):
    return DataStore(db).update({"id": item_id}, models.Item, updated_item.dict())
    # TODO: Create raising of errors for proper handling


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str, db: Session = Depends(get_db)):
    DataStore(db).delete(models.Item, filter={"id": id})
    return {"message": "Item deleted"}

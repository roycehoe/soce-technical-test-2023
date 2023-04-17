from pydantic import BaseModel


class ItemIn(BaseModel):
    """The request body when new items are created"""

    name: str
    number: int
    is_happy: bool


class ItemOut(BaseModel):
    """The response body when items database is queried"""

    name: str
    is_happy: bool

    class Config:
        orm_mode = True

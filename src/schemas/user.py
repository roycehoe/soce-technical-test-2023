from pydantic import BaseModel


class UserIn(BaseModel):
    """The request body when new users are created"""

    name: str
    number: int
    is_happy: bool


class UserOut(BaseModel):
    """The response body when users are queried"""

    name: str
    is_happy: bool

    class Config:
        orm_mode = True

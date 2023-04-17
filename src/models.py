from sqlalchemy import Column, Integer, String

from src.database import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    description = Column(String)

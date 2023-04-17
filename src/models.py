from sqlalchemy import Boolean, Column, Integer, String

from src.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(Integer)
    is_happy = Column(Boolean)

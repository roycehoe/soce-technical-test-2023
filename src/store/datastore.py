from dataclasses import dataclass
from typing import Any, Callable, Optional

from sqlalchemy.orm import Session

from src.schemas.database import Database


def _remove_none_from_dict(func):
    def wrap(*args, **kwargs):
        kwargs["filter"] = {
            key: value for key, value in kwargs["filter"].items() if value is not None
        }
        result = func(*args, **kwargs)
        return result

    return wrap


def _get_order_by(
    model: Any, sort_col: Optional[str], sort_order: Optional[str]
) -> Optional[Callable]:
    if sort_col is None:
        return None

    sort_attr = getattr(model, sort_col)
    if sort_order == "asc":
        return sort_attr.asc()
    return sort_attr.desc()


@dataclass
class DataStore(Database):
    """A class containing all CRUD methods for an SQL database"""

    session: Session

    def create(self, new_row: Any) -> Any:
        with self.session as session:
            session.add(new_row)
            session.commit()
            return new_row

    def create_many(self, new_rows: list[Any]) -> None:
        with self.session as session:
            session.add_all(new_rows)
            session.commit()

    @_remove_none_from_dict
    def get(self, model: Any, *, filter: dict) -> Any:
        return self.session.query(model).filter_by(**filter).all()

    def get_all(self, model: Any) -> list[Any]:
        with self.session as session:
            return session.query(model).all()

    def get_unique(self, model: Any, row_name: str) -> list[Any]:
        with self.session as session:
            return [
                getattr(row_value, row_name)
                for row_value in session.query(getattr(model, row_name)).distinct()
            ]

    def search(
        self,
        model: Any,
        column_name: str,
        q: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort_col: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> list[Any]:
        with self.session as session:
            order_by = _get_order_by(model, sort_col, sort_order)
            return (
                session.query(model)
                .filter(getattr(model, column_name).like(f"{q}%"))
                .order_by(order_by)
                .limit(limit)
                .offset(offset)
                .all()
            )

    def update(self, filter: dict, model: Any, new_row: dict) -> None:
        with self.session as session:
            session.query(model).filter_by(**filter).update(new_row)
            session.commit()

    def delete(self, model: Any, *, filter: dict) -> None:
        with self.session as session:
            session.query(model).filter_by(**filter).delete()
            session.commit()

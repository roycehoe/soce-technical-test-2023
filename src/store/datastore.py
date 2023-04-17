from dataclasses import dataclass
from typing import Any, Callable, Optional

from sqlalchemy.orm import Session

from src.schemas.database import Database


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

    def get(self, model: Any, id: int) -> Optional[Any]:
        if data := self.session.query(model).filter_by(id=id).first():
            return data

        raise Exception(f"No data of model {model} with id {id} found")
        # TODO: Create proper error handling here

    def get_all(self, model: Any) -> list[Any]:
        with self.session as session:
            if data := session.query(model).all():
                return data

            raise Exception(f"No data in model {model} found")

    def get_unique(self, model: Any, column_name: str) -> list[Any]:
        with self.session as session:
            if unique_data := [
                getattr(row_value, column_name)
                for row_value in session.query(getattr(model, column_name)).distinct()
            ]:
                return unique_data

            raise Exception(
                f"No unique data in {model} found with the following column:{column_name}"
            )

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
            if search_results := (
                session.query(model)
                .filter(getattr(model, column_name).like(f"{q}%"))
                .order_by(order_by)
                .limit(limit)
                .offset(offset)
                .all()
            ):
                return search_results
            raise Exception(f"No results found during search")

    def update(self, filter: dict, model: Any, new_row: dict) -> Optional[dict]:
        with self.session as session:
            if db_item := session.query(model).filter_by(**filter).first():
                db_item.update(new_row)
                session.commit()
                return new_row
            raise Exception("Problem updating DB item")
            # TODO: Create proper error handling here

    def delete(self, model: Any, *, filter: dict) -> Optional[dict]:
        with self.session as session:
            if db_item := session.query(model).filter_by(**filter).first():
                db_item.delete()
                session.commit()
                return db_item

            raise Exception("Problem deleting DB item")
            # TODO: Create proper error handling here
